import styles from './Anchor.module.css';

interface AnchorProps {
    children: string,
    href: string,
}

export default function Anchor({ children, href }: AnchorProps) {
    return <a className={styles.anchor} href={href}>{children}</a>
} 