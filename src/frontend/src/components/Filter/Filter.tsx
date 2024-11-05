import { FaSearch } from 'react-icons/fa';
import { IoMdArrowDropdown } from "react-icons/io";
import styles from './Filter.module.css';
import { useEffect, useRef, useState } from 'react';
import Tag from '../Tag/Tag';

interface Option {
    label: string;
    value: any;
}

interface FilterProps {
    children: string;
    options?: Option[];
    selected?: any;
    setSelected: Function;
}

export default function Filter<T>({ children, options, selected, setSelected }: FilterProps) {
    const [currentSelected, setCurrentSelected] = useState<any | undefined>(selected || -1);
    const [optionsVisibility, setOptionsVisibility] = useState(false);
    const dropdownRef = useRef<HTMLDivElement>(null);

    const handleOptionClick = (value: any) => {
        setCurrentSelected(value);
        setSelected(value)
        setOptionsVisibility(false);
    };

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
    }, [dropdownRef]);

    return (
        <div className={styles['select-box']} ref={dropdownRef}>
            <div className={styles['title-div']} onClick={() => setOptionsVisibility(prev => !prev)}>
                <FaSearch className={styles.searchIcon} />
                <span className={styles['title']}>{children}</span>
                {options && options.length > 0 && (
                    <Tag>{options.find(option => option.value === currentSelected)?.label || 'Selecione uma opção'}</Tag>
                )}
                <IoMdArrowDropdown className={`${styles.arrowDropdownIcon} ${optionsVisibility && styles.active}`} />
            </div>
            {optionsVisibility &&
                <div className={styles["options-container"]}>
                    <div className={styles['option']} onClick={() => handleOptionClick(-1)}>
                        Selecione uma opção
                    </div>
                    {options?.map((option, index) => {
                        return (
                            <div key={index} className={styles['option']} onClick={() => handleOptionClick(option.value)}>
                                {option.label}
                            </div>
                        )
                    })}
                </div>
            }
        </div >
    );
}
