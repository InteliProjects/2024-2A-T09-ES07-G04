import Pagination from "@/components/Pagination/Pagination";
import React, { useState } from 'react';
import { render, fireEvent } from '@testing-library/react';

describe('Pagination Component', () => {
    test('renders pagination with correct numeration and handles page changes', () => {
        const totalPages = 14;

        const PaginationWrapper = () => {
            const [currentPage, setCurrentPage] = useState(1);
            return <Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />;
        };

        const { getByText } = render(<PaginationWrapper />);
        expect(getByText('Página 1 de 14')).toBeInTheDocument();
    });

    test('go to previous and next page', () => {
        const totalPages = 3;

        const PaginationWrapper = () => {
            const [currentPage, setCurrentPage] = useState(1);
            return <Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />;
        };

        const { getByText, getByTestId } = render(<PaginationWrapper />);
        const leftButton = getByTestId('left-button');
        const rightButton = getByTestId('right-button');

        expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();

        fireEvent.click(rightButton);
        expect(getByText(`Página 2 de ${totalPages}`)).toBeInTheDocument();

        fireEvent.click(leftButton);
        expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
    });

    test("tries to go to previous page - (it's already the first page)", () => {
        const totalPages = 3;

        const PaginationWrapper = () => {
            const [currentPage, setCurrentPage] = useState(1);
            return <Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />;
        };

        const { getByText, getByTestId } = render(<PaginationWrapper />);
        const leftButton = getByTestId('left-button');

        expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
        fireEvent.click(leftButton);
        expect(getByText(`Página 1 de ${totalPages}`)).toBeInTheDocument();
    });

    test("tries to go to next page - (it's already the last page)", () => {
        const totalPages = 3;

        const PaginationWrapper = () => {
            const [currentPage, setCurrentPage] = useState(3);
            return <Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />;
        };

        const { getByText, getByTestId } = render(<PaginationWrapper />);
        const rightButton = getByTestId('right-button');

        expect(getByText(`Página 3 de ${totalPages}`)).toBeInTheDocument();
        fireEvent.click(rightButton);
        expect(getByText(`Página 3 de ${totalPages}`)).toBeInTheDocument();
    });
});
