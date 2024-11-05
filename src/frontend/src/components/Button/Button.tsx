import styles from './Button.module.css';

interface ButtonProps {
    children: string,
    onClick: Function,
    icon?: React.ReactNode,
}

export default function Button({ children, onClick, icon }: ButtonProps) {
    return <button className={styles.button} onClick={() => onClick()}>
        {icon ? <div className={styles["icon-div"]}>{icon}</div> : null}
        {children}
    </button>
} 