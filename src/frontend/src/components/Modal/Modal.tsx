import styles from './Modal.module.css'

interface ModalProps {
    children?: React.ReactNode,
    visibility: boolean,
    setVisibility: React.Dispatch<React.SetStateAction<boolean>>,
}

export default function Modal({ children, visibility, setVisibility }: ModalProps) {
    if (!visibility) return;

    return (
        <>
            <div className={styles.bg} onClick={() => {setVisibility(false)}}/>
            <div className={styles.modal}>
                {children}
            </div>
        </>
    )
}