import { fireEvent, getByLabelText, render, screen } from '@testing-library/react';
import Sidebar from '@/components/Sidebar/Sidebar';
import { useRouter } from 'next/router';
import styles from './Sidebar.module.css';

// Mocking the Next.js useRouter hook to control routing behavior in tests
jest.mock('next/router', () => ({
    useRouter: jest.fn(),
}));

describe('Sidebar Component', () => {
    test('renders sidebar with menu button and all items', () => {
        // Rendering the Sidebar component and capturing the container and test IDs
        const { container, getByTestId } = render(<Sidebar />);

        // Selecting sidebar and buttons using CSS class and data-testid attributes
        const sidebar = container.querySelector(`.${styles.sidebar}`);
        const toggleButton = container.querySelector(`.${styles.menuBtn}`);
        const homeButton = getByTestId('home-button');
        const explorerButton = getByTestId('explorer-button');
        const tagButton = getByTestId('tag-button');
        const regulatorsDiv = container.querySelector(`.${styles.regulators}`);

        // Assertions to verify that elements are rendered correctly
        expect(toggleButton).toBeInTheDocument();
        expect(homeButton).toBeInTheDocument();
        expect(explorerButton).toBeInTheDocument();
        expect(tagButton).toBeInTheDocument();
        expect(sidebar).toBeInTheDocument();
        expect(regulatorsDiv).toBeInTheDocument();
    });

    test('open and close sidebar', () => {
        const { container } = render(<Sidebar />);
        const sidebar = container.querySelector(`.${styles.sidebar}`);
        const toggleButton = container.querySelector(`.${styles.menuBtn}`);

        // Ensure the sidebar is initially not expanded
        expect(sidebar).not.toHaveClass(styles.expanded);
        fireEvent.click(toggleButton!); // Simulate click to open sidebar
        expect(sidebar).toHaveClass(styles.expanded); // Verify sidebar is expanded
        fireEvent.click(toggleButton!); // Simulate click to close sidebar
        expect(sidebar).not.toHaveClass(styles.expanded); // Verify sidebar is closed
    });

    test('go to explorer', () => {
        const pushMock = jest.fn(); // Create a mock function for router push

        // Mocking useRouter to simulate navigation behavior
        (useRouter as jest.Mock).mockImplementation(() => ({
            route: '/',
            pathname: '/',
            query: {},
            asPath: '/',
            push: pushMock, // Assign the mock function to push
        }));

        const { getByTestId } = render(<Sidebar />);
        const explorerButton = getByTestId('explorer-button');
        fireEvent.click(explorerButton!); // Simulate click on explorer button

        // Verify that the push function was called with the correct path
        expect(pushMock).toHaveBeenCalledWith('/regulations');
    });

    test('go to home', () => {
        const pushMock = jest.fn(); // Create a mock function for router push

        // Mocking useRouter with current route set to '/regulations'
        (useRouter as jest.Mock).mockImplementation(() => ({
            route: '/regulations',
            pathname: '/regulations',
            query: {},
            asPath: '/regulations',
            push: pushMock,
        }));

        const { getByTestId } = render(<Sidebar />);
        const homeButton = getByTestId('home-button');
        fireEvent.click(homeButton!); // Simulate click on home button

        // Verify that the push function was called to navigate to home
        expect(pushMock).toHaveBeenCalledWith('/');
    });

    test('go to tag page', () => {
        const pushMock = jest.fn(); // Create a mock function for router push

        // Mocking useRouter to simulate navigation behavior
        (useRouter as jest.Mock).mockImplementation(() => ({
            route: '/',
            pathname: '/',
            query: {},
            asPath: '/',
            push: pushMock,
        }));

        const { getByTestId } = render(<Sidebar />);
        const tagButton = getByTestId('tag-button');
        fireEvent.click(tagButton!); // Simulate click on tag button

        // Verify that the push function was called with the correct path
        expect(pushMock).toHaveBeenCalledWith('/tags');
    });

    test('go to regulator page', () => {
        const openMock = jest.fn(); // Mock function for window.open
        window.open = openMock; // Overriding the window.open method

        const { getByTestId } = render(<Sidebar />);
        const regulatorButton = getByTestId('regulator-button');
        fireEvent.click(regulatorButton!); // Simulate click on regulator button

        // Verify that window.open was called with the correct URL and target
        expect(openMock).toHaveBeenCalledWith('https://www.bcb.gov.br/', '_blank');
    });
});
