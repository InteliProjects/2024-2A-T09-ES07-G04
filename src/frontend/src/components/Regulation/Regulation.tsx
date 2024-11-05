import React, { useEffect } from 'react';
import styles from './Regulation.module.css'
import Tag from '../Tag/Tag';
import { formatDate, formatNumberWithDots } from '@/utils/helpers';
import { useRouter } from 'next/router';
import { Regulation as RegulationType } from '@/types/regulation.type';

export default function Regulation({ regulation }: { regulation: RegulationType }) {
    const router = useRouter();

    function openCard() {
        router.push(`regulations/${regulation.id}`)
    };

    return (
        <div className={styles.card} onClick={openCard}>
            <div className={styles.head}>
                <h1 className={styles.title} onClick={event => { event.stopPropagation() }}>{regulation.documenttype_name} nº {formatNumberWithDots(regulation.documentnumber)}</h1>
                <span className={styles.date}>{formatDate(regulation.publicationdate)}</span>
            </div>
            <p className={styles.subject} onClick={event => { event.stopPropagation() }}>{regulation.topic}</p>
            {regulation.tags.length > 0 ?
                <div className={styles['tags-div']}>
                    {regulation.tags.map((tag, index: number) =>
                        <Tag key={index} width='min-content' maxWidth='20rem'>{tag}</Tag>
                    )}
                </div>
                :
                null
            }
        </div>
    );
};
