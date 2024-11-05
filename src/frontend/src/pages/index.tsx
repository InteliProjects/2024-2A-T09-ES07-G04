import React from 'react';
import Dashboard from '../components/Dashboard/Dashboard';
import MainLayout from '@/layouts/MainLayout/MainLayout';

export default function Home() {
	return (
		<MainLayout>
			<Dashboard />
		</MainLayout>
	);
};
