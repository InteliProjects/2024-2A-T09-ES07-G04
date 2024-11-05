import styles from './Tag.module.css'

interface TagProps {
    children: string,
    width?: string,
    maxWidth?: string,
}

export default function Tag({ children, width = '5rem', maxWidth }: TagProps) {
    return (
        <div className={styles['tag']} style={{ maxWidth, width }}>{children}</div>
    );
};
