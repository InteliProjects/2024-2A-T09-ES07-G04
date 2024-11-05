import Sidebar from '@/components/Sidebar/Sidebar'
import styles from './MainLayout.module.css'
import { useEffect, useState } from 'react';

export default function MainLayout({ children }: { children?: React.ReactNode }) {
    const [isExpanded, setIsExpanded] = useState(false);

    return <>
        <Sidebar isExpanded={isExpanded} setIsExpanded={setIsExpanded} />
        <div className={`${styles['main']} ${isExpanded && styles.expanded}`}>
            {children}
        </div>
    </>
}
