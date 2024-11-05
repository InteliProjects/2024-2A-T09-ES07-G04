import styles from './SearchHead.module.css';
import LogoSVG from '@/components/svgs/LogoSVG/LogoSVG';
import SearchBar from '@/components/Searchbar/Searchbar';
import { useRouter } from 'next/router';

export default function SearchHead({onClick}: {onClick: Function}) {
    const router = useRouter();

    return (
        <div className={styles['search-head']}>
            <div className={styles['logo-container']} onClick={() => router.push('/')}><LogoSVG /></div>
            <SearchBar onClick={onClick}/>
        </div>
    );
}
