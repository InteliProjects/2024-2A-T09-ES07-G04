import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import Microphone from '@/components/Microphone/Microphone';
import { useRouter } from 'next/router';

// Mocking necessary hooks and functions
jest.mock('next/router', () => ({
  useRouter: jest.fn(),
}));

// Mocking navigator.mediaDevices.getUserMedia API
const mockGetUserMedia = jest.fn();

Object.defineProperty(global.navigator, 'mediaDevices', {
  value: {
    getUserMedia: mockGetUserMedia,
  },
});

// Mocking MediaRecorder
class MockMediaRecorder {
  state = 'inactive';
  ondataavailable: (event: { data: Blob }) => void = () => { };
  onstop: () => void = () => { };
  audioChunks: Blob[] = [];

  constructor(stream: MediaStream) {
    this.state = 'inactive';
  }

  start() {
    this.state = 'recording';
  }

  stop() {
    this.state = 'inactive';
    if (this.onstop) {
      this.onstop();
    }
    this.ondataavailable({ data: new Blob(['audio data'], { type: 'audio/webm' }) });
  }
}

global.MediaRecorder = MockMediaRecorder as any; // Mocking the global MediaRecorder object

describe('Microphone Component', () => {
  let mockSetIsRecording: jest.Mock;
  let mockSetIsProcessing: jest.Mock;
  let mockSetHasError: jest.Mock;

  beforeEach(() => {
    mockSetIsRecording = jest.fn();
    mockSetIsProcessing = jest.fn();
    mockSetHasError = jest.fn();

    // Reset mocks before each test
    (useRouter as jest.Mock).mockReturnValue({ push: jest.fn() });
    mockGetUserMedia.mockClear();
  });

  test('should render microphone button', () => {
    render(
      <Microphone
        setIsRecording={mockSetIsRecording}
        setIsProcessing={mockSetIsProcessing}
        setHasError={mockSetHasError}
      />
    );

    const micButton = screen.getByRole('button');
    expect(micButton).toBeInTheDocument();
  });

  test('should start recording on click', async () => {
    const mockStream = { getTracks: jest.fn(() => [{ stop: jest.fn() }]) };
    mockGetUserMedia.mockResolvedValue(mockStream);

    render(
      <Microphone
        setIsRecording={mockSetIsRecording}
        setIsProcessing={mockSetIsProcessing}
        setHasError={mockSetHasError}
      />
    );

    const micButton = screen.getByRole('button');
    fireEvent.click(micButton);

    await waitFor(() => {
      expect(mockSetIsRecording).toHaveBeenCalledWith(true);
      expect(mockGetUserMedia).toHaveBeenCalledWith({ audio: true });
    });
  });

  test('should stop recording on click when already recording', async () => {
    const mockStream = { getTracks: jest.fn(() => [{ stop: jest.fn() }]) };
    mockGetUserMedia.mockResolvedValue(mockStream);

    render(
      <Microphone
        setIsRecording={mockSetIsRecording}
        setIsProcessing={mockSetIsProcessing}
        setHasError={mockSetHasError}
      />
    );

    const micButton = screen.getByRole('button');

    fireEvent.click(micButton); // Start recording
    await waitFor(() => {
      expect(mockSetIsRecording).toHaveBeenCalledWith(true);
    });

    fireEvent.click(micButton); // Stop recording
    await waitFor(() => {
      expect(mockSetIsRecording).toHaveBeenCalledWith(false);
    });
  });

  test('should handle media recorder errors', async () => {
    // Simulating a permission denied error
    mockGetUserMedia.mockRejectedValueOnce(new Error('Permission denied'));

    render(
      <Microphone
        setIsRecording={mockSetIsRecording}
        setIsProcessing={mockSetIsProcessing}
        setHasError={mockSetHasError}
      />
    );

    const micButton = screen.getByRole('button');

    // simulating a click on the microphone button
    fireEvent.click(micButton);

    // verifying if the error was handled correctly
    await waitFor(() => {
      expect(mockSetIsRecording).toHaveBeenCalledWith(false);
      expect(mockSetHasError).toHaveBeenCalledWith(true);
    });
  });

});
