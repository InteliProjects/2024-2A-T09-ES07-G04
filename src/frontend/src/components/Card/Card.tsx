// components/Card.js
import React from 'react';
import { IoSearch } from "react-icons/io5";
import styles from './Card.module.css';

const Card = ({ text }: { text: string }) => {
	return (
		<div className={styles.card}>
			<IoSearch className={styles.cardIcon} />
			<p>{text}</p>
		</div>
	);
};

export default Card;