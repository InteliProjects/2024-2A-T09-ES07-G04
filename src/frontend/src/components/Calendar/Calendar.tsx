import { FaSearch } from 'react-icons/fa';
import { IoMdArrowDropdown } from "react-icons/io";
import styles from './Calendar.module.css';
import { useEffect, useRef, useState } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';


interface CalendarFilterProps {
    children: string;
    setSelected: Function;
}

export default function CalendarFilter({ children, setSelected }: CalendarFilterProps) {
    const [optionsVisibility, setOptionsVisibility] = useState(false);
    const [startDate, setStartDate] = useState<Date | null>(null);
    const [endDate, setEndDate] = useState<Date | null>(null);
    const dropdownRef = useRef<HTMLDivElement>(null);

    const toggleVisibility = () => setOptionsVisibility(!optionsVisibility);

    useEffect(() => {
        if (endDate && startDate) {
            setSelected({end: endDate, start: startDate})
        } else {
            setSelected(null)
        }
    }, [endDate, startDate])

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
                setOptionsVisibility(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

    return (
        <div className={styles['select-box']} ref={dropdownRef}>
            <div className={styles['title-div']} onClick={toggleVisibility}>
                <FaSearch className={styles.searchIcon} />
                <span className={styles['title']}>{children}</span>
                <span className={styles['selected-range']}>
                    {startDate && endDate ? `${startDate.toLocaleDateString()} - ${endDate.toLocaleDateString()}` : 'Selecione o período'}
                </span>
                <IoMdArrowDropdown className={styles.arrowDropdownIcon} />
            </div>

            {optionsVisibility && (
                <div className={styles["options-container"]}>
                    <DatePicker
                        selected={startDate}
                        onChange={(dates) => {
                            const [start, end] = dates as [Date | null, Date | null];
                            setStartDate(start);
                            setEndDate(end);
                        }}
                        startDate={startDate || undefined}
                        endDate={endDate || undefined}
                        selectsRange
                        inline
                    />
                </div>
            )}
        </div>
    );
}
