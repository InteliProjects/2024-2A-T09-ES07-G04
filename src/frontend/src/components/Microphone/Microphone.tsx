import { FaMicrophone } from 'react-icons/fa';
import styles from './Microphone.module.css';
import { useState } from 'react';
import { inputStore } from '../../store/input.store';
import { useRouter } from 'next/router';

interface MicrophoneProps {
    setIsRecording: (value: boolean) => void;
    setIsProcessing: (value: boolean) => void;
    setHasError: (value: boolean) => void;
}

export default function Microphone({ setIsRecording, setIsProcessing, setHasError }: MicrophoneProps) {
    const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
    const { setInputText } = inputStore();
    const router = useRouter();

    let audioChunks: Blob[] = [];

    const startRecording = async () => {
        try{
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const recorder = new MediaRecorder(stream, {
            mimeType: 'audio/webm;codecs=opus'
        });

        recorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        setIsRecording(true);
        setHasError(false);

        recorder.onstop = () => {
            if (audioChunks.length > 0) {
                const audioBlob = new Blob(audioChunks, { type: 'audio/webm;codecs=opus' });
                setIsProcessing(true);
                transcribe(audioBlob);
                audioChunks = [];
            }

            stream.getTracks().forEach(track => track.stop());
        };

        setMediaRecorder(recorder);
        recorder.start();
    } catch (error) {
        console.error('Error accessing media devices:', error);
        setIsRecording(false);
        setHasError(true);
    }
};

    const stopRecording = () => {
        if (mediaRecorder) {
            mediaRecorder.stop();
        }
        setIsRecording(false);
    };

    const handleRecorder = () => {
        if (mediaRecorder && mediaRecorder.state === "recording") {
            stopRecording();
        } else {
            startRecording();
        }
    };


    async function transcribe(audioUrl: Blob) {
        try {
            const formData = new FormData();
            formData.append('audio', audioUrl, 'recording.webm');

            const response = await fetch('http://localhost:5002/audio/transcribe', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                const transcriptText = data.results[0].alternatives[0].transcript;
                setInputText(transcriptText);
                setIsProcessing(false);
                router.push('/regulations');
            } else {
                setIsProcessing(false);
                setHasError(true);
            }
        } catch (error) {
            setIsProcessing(false);
            setHasError(true);
        }
    }

    return (
        <button className={styles.button} onClick={handleRecorder}>
            <FaMicrophone className={`${styles.microphoneIcon} ${mediaRecorder && mediaRecorder.state === "recording" ? styles.active : ''}`} />
        </button>
    );
}
