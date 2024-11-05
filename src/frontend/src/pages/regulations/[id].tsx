import { FaArrowLeftLong } from "react-icons/fa6";
import { formatDate, formatNumberWithDots } from '@/utils/helpers';
import { useRouter } from 'next/router';
import React, { useEffect, useState } from 'react';
import Topic from '@/components/Topic/Topic';
import MainLayout from '@/layouts/MainLayout/MainLayout';
import Information from '@/components/Information/Information';
import styles from './id.module.css';
import RegulationInformationCard from "@/components/RegulationInformationCard/RegulationInformationCard";
import { Regulation } from "@/types/regulation.type";
import Loader from "@/components/Loader/Loader";

/**
 * Page component to display details about a specific regulation.
 * Fetches regulation data based on the `id` parameter from the URL.
 */
export default function RegulationPage() {
    const router = useRouter();
    const { id } = router.query;

    // State for regulation data, loading status, and error handling
    const [regulation, setRegulation] = useState<Regulation>();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch regulation data when `id` changes
    useEffect(() => {
        if (id) {
            setLoading(true);
            fetch(`http://localhost:5002/regulations/${id}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`Erro HTTP! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    setRegulation(data);
                    setLoading(false);
                })
                .catch(error => {
                    setError(error.message);
                    setLoading(false);
                });
        }
    }, [id]);

    // Handle case where regulation is not found
    if (loading === false && !regulation) {
        return <p>Regulamento não encontrado.</p>;
    }

    return (
        <MainLayout>
            {loading ?
                <Loader />
                :
                regulation &&
                <main className={styles.main}>
                    <section className={styles['content-section']}>
                        <FaArrowLeftLong className={styles.arrowBackIcon} onClick={() => router.push('/regulations')} />
                        <Topic>{`${regulation.documenttype_name} nº ${formatNumberWithDots(regulation.documentnumber)}`}</Topic>
                        <div className={styles['information-div']}>
                            <Information label='Regulador' value={'BACEN'} />
                            <Information label='Data' value={formatDate(regulation.publicationdate)} />
                        </div>
                        <div className={styles.description} dangerouslySetInnerHTML={{ __html: regulation.xmltext }} />
                    </section>
                    <section className={styles['information-section']}>
                        <RegulationInformationCard regulation={regulation} />
                    </section>
                </main>
            }
        </MainLayout>
    );
};
