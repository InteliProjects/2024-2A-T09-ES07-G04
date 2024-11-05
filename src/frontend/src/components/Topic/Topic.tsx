import styles from './Topic.module.css';

interface TopicProps {
    children: string,
    subTitle?: string,
}

export default function Topic({ children, subTitle }: TopicProps) {
    return (
        <div className={styles['topic-container']}>
            <h1 className={styles.title}>{children}</h1>
            <h2 className={styles.subtitle}>{subTitle}</h2>
        </div>
    );
}
