import React from 'react';
import Image from 'next/image';
import SearchBar from '../Searchbar/Searchbar';
import Card from '../Card/Card';
import styles from './Dashboard.module.css'
import { inputStore } from '@/store/input.store';
import { useRouter } from 'next/router';

export default function Dashboard() {
	const { setGetAutomatic, setInputText, inputText } = inputStore();
	const router = useRouter();

	return (
		<div className={`${styles.dashboard}`}>
			<div className={styles.logoContainer}>
				<Image
					src="/svgs/logo.svg"
					alt="VOX Logo"
					width={200}
					height={0}
					className={styles.logo}
				/>
			</div>

			<div className={styles['searchbar-container']}>
				<SearchBar onClick={() => {
					setInputText(inputText);
					setGetAutomatic(true);
					router.push('/regulations');
				}} />
			</div>

			<div className={styles.quickSearch}>
				<Card text="Mostre as atualizações do dia" />
				<Card text="Mostre as últimas normas do BACEN" />
				<Card text="Mostre-me as atualizações do dia" />
				<Card text="Mostre-me as atualizações do dia" />
			</div>
		</div>
	);
};
