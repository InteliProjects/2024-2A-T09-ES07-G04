import styles from './Information.module.css';

interface InformationProps {
    label: string,
    value: string | number,
}

export default function Information({ label, value }: InformationProps) {
    return (
        <p>
            <span className={styles['label']}>{label}: </span>
            <span className={styles['value']}>{value}</span>
        </p>
    )
}
