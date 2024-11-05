import { SlArrowLeft, SlArrowRight } from "react-icons/sl";
import styles from './Pagination.module.css';

interface PaginationProps {
    current: number;
    total: number;
    setCurrent: React.Dispatch<React.SetStateAction<number>>
}

export default function Pagination({ current, total, setCurrent }: PaginationProps) {
    function handlePageChange(newPage: number) {
        if (newPage > 0 && newPage <= total) {
            setCurrent(newPage);
        }
    };

    return (
        <div className={styles.pagination}>
            <button data-testid='left-button' className={current === 1 ? styles['disabled-button'] : ''} onClick={() => handlePageChange(current - 1)}>
                <SlArrowLeft className={styles.icon} />
            </button>
            <span>
                Página {current} de {total}
            </span>
            <button data-testid='right-button' className={current === total ? styles['disabled-button'] : ''} onClick={() => handlePageChange(current + 1)}>
                <SlArrowRight className={styles.icon} />
            </button>
        </div>
    )
}