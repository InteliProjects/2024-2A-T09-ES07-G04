import React, { useEffect, useState } from 'react';
import MainLayout from '@/layouts/MainLayout/MainLayout';
import Searchbar from '@/components/Searchbar/Searchbar';
import Topic from '@/components/Topic/Topic';
import styles from './TagPage.module.css';
import Pagination from '@/components/Pagination/Pagination';
import Loader from '@/components/Loader/Loader';
import { FaEdit, FaTrash } from 'react-icons/fa';
import { Tag } from '@/types/filters.type';
import Modal from '@/components/Modal/modal';

const ITEMS_PER_PAGE = 10;

export default function TagsPage() {
    const [tags, setTags] = useState<Tag[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const [modalVisibility, setModalVisibility] = useState(false);

    useEffect(() => {
        const fetchTags = async () => {
            setLoading(true);
            try {
                const response = await fetch('http://localhost:5002/tags');
                if (!response.ok) {
                    throw new Error('Failed to fetch tags');
                }
                const data = await response.json();
                setTags(data);
            } catch (error) {
                console.error('Error fetching tags:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchTags();
    }, []);

    const indexOfLastItem = currentPage * ITEMS_PER_PAGE;
    const indexOfFirstItem = indexOfLastItem - ITEMS_PER_PAGE;
    const currentItems = tags.slice(indexOfFirstItem, indexOfLastItem);

    const totalPages = Math.ceil(tags.length / ITEMS_PER_PAGE) || 1;

    const handleDelete = async (tagId: number) => {
        if (window.confirm('Are you sure you want to delete this tag?')) {
            try {
                const response = await fetch(`http://localhost:5002/tags/${tagId}`, {
                    method: 'DELETE',
                });
                if (!response.ok) {
                    throw new Error('Failed to delete tag');
                }
                setTags(tags.filter(tag => tag.id !== tagId));
            } catch (error) {
                console.error('Error deleting tag:', error);
            }
        }
    };

    return (
        <MainLayout>
            {loading ? (
                <Loader />
            ) : (
                <>
                    <div className={styles.header}>
                        <div className={styles.titleContainer}>
                            <Topic>Tags</Topic>
                            <p className={styles.subTitle}>Total de Tags: {tags.length}</p>
                        </div>
                        <button className={styles.addTagButton} onClick={() => { setModalVisibility(true) }}>Adicionar tag</button>
                    </div>

                    <Searchbar onClick={() => { }} type="tags" />

                    <main className={styles.main}>
                        <table className={styles.tagsTable}>
                            <thead>
                                <tr>
                                    <th>Nome</th>
                                    <th>Ações</th>
                                </tr>
                            </thead>
                            <tbody>
                                {currentItems.length > 0 ? (
                                    currentItems.map((tag) => (
                                        <tr key={tag.id}>
                                            <td>{tag.name}</td>
                                            <td className={styles.actions}>
                                                <button className={styles['edit-btn']}>
                                                    <FaEdit />
                                                </button>
                                                <button
                                                    className={styles['delete-btn']}
                                                    onClick={() => handleDelete(tag.id)}
                                                >
                                                    <FaTrash />
                                                </button>
                                            </td>
                                        </tr>
                                    ))
                                ) : (
                                    <tr>
                                        <td colSpan={3}>Nenhuma tag encontrada.</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>

                        <div className={styles.footer}>
                            {currentItems.length ? (
                                <Pagination current={currentPage} total={totalPages} setCurrent={setCurrentPage} />
                            ) : null}
                        </div>
                    </main>
                </>
            )}
            <Modal setVisibility={setModalVisibility} visibility={modalVisibility}>
                <h1>Adicionar tag</h1>
            </Modal>
            <Modal setVisibility={setModalVisibility} visibility={modalVisibility}>

            </Modal>
        </MainLayout>
    );
}
