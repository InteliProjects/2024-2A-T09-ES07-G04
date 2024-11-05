import React, { useEffect, useState } from 'react';
import MainLayout from '@/layouts/MainLayout/MainLayout';
import SearchHead from '@/components/SearchHead/SearchHead';
import Topic from '@/components/Topic/Topic';
import Filter from '@/components/Filter/Filter';
import styles from './regulations.module.css';
import { formatNumberWithDots } from '@/utils/helpers';
import Loader from '@/components/Loader/Loader';
import { inputStore } from '@/store/input.store';
import CalendarFilter from '@/components/Calendar/Calendar';
import { dataStore } from '@/store/data.store';
import Pagination from '@/components/Pagination/Pagination';
import { Filters } from '@/types/filters.type';
import { Regulation as RegulationType } from '@/types/regulation.type';
import Regulation from '@/components/Regulation/Regulation';

const ITEMS_PER_PAGE = 10;

export default function Regulations() {
	const { inputText, getAutomatic, setGetAutomatic } = inputStore();
	const { data, setData } = dataStore();
	const [loading, setLoading] = useState(true);
	const [currentPage, setCurrentPage] = useState(1);
	const [tags, setTags] = useState<{ value: any; label: any }[]>([]);
	const [regulators, setRegulators] = useState<{ value: any; label: any }[]>([]);
	const [selectedRegulator, setSelectedRegulator] = useState<number | null>(null);
	const [selectedTag, setSelectedTag] = useState<number | null>(null);
	const [selectedDateInterval, setSelectedDateInterval] = useState<{ end: Date, start: Date } | null>(null);
	const [filteredRegulations, setFilteredRegulations] = useState<RegulationType[]>([]);

	// Fetch filters on component mount
	useEffect(() => {
		const fetchFilters = async () => {
			const response = await fetch('http://127.0.0.1:5002/filters', { method: 'GET' });
			if (response.ok) {
				const filters: Filters = await response.json();
				setTags(filters.tags.map(tag => ({ value: tag.id, label: tag.name })));
				setRegulators(filters.regulators.map(regulator => ({ value: regulator.id, label: regulator.name })));
			}
		};

		fetchFilters();
	}, []);

	// Fetch regulations based on input text when the component mounts or when inputText changes
	useEffect(() => {
		if (getAutomatic) {
			setGetAutomatic(false);
			fetchRegulations(inputText);
		} else {
			setLoading(false);
		}
	}, [inputText]);

	// Fetch regulations from the API
	const fetchRegulations = async (query: string) => {
		setLoading(true);
		console.log('mano')
		try {
			const response = await fetch('http://127.0.0.1:5000/pln/query', {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ input: query })
			});

			if (!response.ok) {
				alert(`HTTP Error! Status: ${response.status}`);
				return;
			}

			const data = await response.json();
			setData(data);
			console.log('data', data)
			setCurrentPage(1); // Reset to first page
			resetFilters();
		} catch (error) {
			console.error('Error fetching regulations:', error);
		} finally {
			setLoading(false);
		}
	};

	function resetFilters() {
		setSelectedDateInterval(null);
		setSelectedRegulator(null);
		setSelectedTag(null);
	}

	// Apply filters to regulations
	const applyFilters = (regulations: RegulationType[]) => {
		let filtered = regulations;

		if (selectedTag !== null) {
			const tag = tags.find(tag => tag.value === selectedTag);
			if (tag) {
				filtered = filtered.filter(regulation => regulation.tags.includes(tag.label));
			}
		}

		if (selectedRegulator !== null) {
			const regulator = regulators.find(regulator => regulator.value === selectedRegulator);
			if (regulator) {
				filtered = filtered.filter(regulation => regulation.regulator_name === regulator.label);
			}
		}

		if (selectedDateInterval !== null) {
			const { start, end } = selectedDateInterval;
			const formatDate = (date: Date) => date.toISOString().split('T')[0];
			filtered = filtered.filter(regulation => {
				const regulationDate = new Date(regulation.publicationdate);

				return formatDate(regulationDate) >= formatDate(start) && formatDate(regulationDate) <= formatDate(end);
			});
		}

		setFilteredRegulations(filtered);
		setCurrentPage(1);
	};

	useEffect(() => {
		applyFilters(data.regulations);
	}, [selectedTag, selectedRegulator, selectedDateInterval, data.regulations]);

	const indexOfLastItem = currentPage * ITEMS_PER_PAGE;
	const indexOfFirstItem = indexOfLastItem - ITEMS_PER_PAGE;
	const currentItems = filteredRegulations.slice(indexOfFirstItem, indexOfLastItem);
	const totalPages = Math.ceil(filteredRegulations.length / ITEMS_PER_PAGE) || 1;

	const regulationQuantityText = (quantity: number) => {
		if (quantity === 1) return `${formatNumberWithDots(quantity)} regulamento encontrado`;
		if (quantity === 0) return 'Nenhum regulamento encontrado';
		return `${formatNumberWithDots(quantity)} regulamentos encontrados`;
	};

	return (
		<MainLayout>
			{loading ? (
				<Loader />
			) : (
				<>
					<SearchHead onClick={() => fetchRegulations(inputText)} />
					<main className={styles.main}>
						<div className={styles.header}>
							<Topic subTitle={regulationQuantityText(filteredRegulations.length)}>Regulamentos</Topic>
							{currentItems.length ? (
								<div className={styles.pagination}>
									<Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />
								</div>
							) : null}
						</div>
						<div className={styles.filter}>
							<Filter options={regulators} setSelected={setSelectedRegulator}>Regulador:</Filter>
							<CalendarFilter setSelected={(value: { end: Date, start: Date } | null) => setSelectedDateInterval(value)}>Período:</CalendarFilter>
							<Filter options={tags} setSelected={setSelectedTag}>Tags:</Filter>
						</div>

						{/* Display list of regulations or message if none are found */}
						<div className={styles['regulations-div']}>
							{currentItems.length > 0 ? (
								currentItems.map((regulation) => (
									<Regulation key={regulation.id} regulation={regulation} />
								))
							) : (
								<p>Nenhum regulamento encontrado.</p>
							)}
						</div>
						<div className={styles.footer}>
							{currentItems.length ? (
								<div>
									<Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />
								</div>
							) : null}
						</div>
					</main>
				</>
			)}
		</MainLayout>
	);
}
