import React, { useEffect, useState } from 'react';
import { FaSearch } from 'react-icons/fa';
import styles from './Searchbar.module.css'
import Microphone from '../Microphone/Microphone';
import { inputStore } from '../../store/input.store';

export default function SearchBar({ onClick = () => { }, type = 'normas' }: { onClick?: Function, type?: 'normas' | 'tags' }) {
    const { inputText, setInputText } = inputStore();
    const [isRecording, setIsRecording] = useState(false);
    const [isProcessing, setIsProcessing] = useState(false);
    const [hasError, setHasError] = useState(false);
    const [placeholder, setPlaceholder] = useState(type === 'normas' ? "Quais regulamentações deseja encontrar?" : "Pesquise uma tag");

    useEffect(() => {
        if (type === 'normas') { 
            if (isRecording) {
                setPlaceholder("Gravando... Fale agora");
            } else if (isProcessing) {
                setPlaceholder("Processando áudio...");
            } else if (hasError) {
                setPlaceholder("Erro ao transcrever o áudio, tente novamente.");
            } else {
                setPlaceholder("Quais regulamentações deseja encontrar?");
            }
        } else {
            setPlaceholder("Pesquise uma tag"); 
        }
    }, [isRecording, isProcessing, hasError, type]);

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInputText(e.target.value);
    };

    const searchBarClass = type === 'tags' ? styles.tagsStyle : styles.searchBar;

    return (
        <div className={`${searchBarClass} ${isRecording ? styles.recording : ''} ${isProcessing ? styles.processing : ''} ${hasError ? styles.error : ''}`}>
            <input
                value={inputText}
                onChange={handleInputChange}
                type="text"
                data-testid="input"
                placeholder={placeholder}
                disabled={type === 'normas' && (isRecording || isProcessing)}
                onKeyDown={(event) => {
                    if (event.key === 'Enter') {
                        onClick();
                    }
                }}
            />
            <div className={styles['buttons-container']}>
                <FaSearch data-testid="search-button" className={styles.searchIcon} onClick={() => onClick()} />
                {type === 'normas' && (
                <Microphone setIsRecording={setIsRecording} setIsProcessing={setIsProcessing} setHasError={setHasError} />
                )}
            </div>
        </div>
    );
}