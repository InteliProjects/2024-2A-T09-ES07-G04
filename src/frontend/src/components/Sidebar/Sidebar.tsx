import React, { useState } from 'react';
import { FaPlus } from 'react-icons/fa';
import { AiOutlineMenu, AiOutlineBank } from 'react-icons/ai';
import { LuHome } from 'react-icons/lu';
import { IoSearch } from 'react-icons/io5';
import { TbTag } from 'react-icons/tb';
import styles from './Sidebar.module.css';
import { useRouter } from 'next/router';

interface SidebarProps {
  isExpanded: boolean;
  setIsExpanded: (isExpanded: boolean) => void;
}

const Sidebar = ({ isExpanded, setIsExpanded }: SidebarProps) => {
  const router = useRouter();

  const toggleSidebar = () => {
    setIsExpanded(!isExpanded);
  };

  const goToHomePage = () => {
    router.push('/');
  };

  const goToRegulationPage = () => {
    router.push('/regulations');
  };

  const goToTagPage = () => {
    router.push('/tags');
  };

  return (
    <>
      <div data-testid='sidebar' className={`${styles.sidebar} ${isExpanded ? styles.expanded : ''}`}>
        {/* Header da sidebar */}
        <div className={styles.sidebarHeader}>
          <button aria-label="Toggle Sidebar" className={styles.menuBtn} onClick={toggleSidebar}>
            <AiOutlineMenu />
          </button>
        </div>

        {/* Itens de navegação */}
        <div className={styles.menuItems}>
          <div className={styles.navItem}>
            <div data-testid='home-button' className={`${styles.icon} ${styles.home}`} onClick={goToHomePage}>
              <LuHome />
            </div>
            <span onClick={goToHomePage}>Home</span>
          </div>

          <div className={styles.navItem}>
            <div data-testid='explorer-button' className={styles.icon} onClick={goToRegulationPage}>
              <IoSearch />
            </div>
            <span onClick={goToRegulationPage}>Explorar</span>
          </div>

          <div className={styles.navItem}>
            <div data-testid='tag-button' className={styles.icon} onClick={goToTagPage}>
              <TbTag />
            </div>
            <span onClick={goToTagPage}>Tags</span>
          </div>

          {/* Alterna entre o divider no modo recolhido e o título "Reguladores" no modo expandido */}
          <div className={styles.regulatorsHeader}>
            {isExpanded ? <h4>Reguladores</h4> : <div className={styles.divider}></div>}
          </div>

          {/* Reguladores */}
          <div className={styles.regulators}>
            <div data-testid='regulator-button' className={styles.navItem} onClick={() => window.open('https://www.bcb.gov.br/', '_blank')}>
              <div className={styles.icon}>
                <AiOutlineBank />
              </div>
              <span>BACEN</span>
            </div>
            <div className={styles.navItem} onClick={() => window.open('https://www.gov.br/cvm/pt-br', '_blank')}>
              <div className={styles.icon}>
                <AiOutlineBank />
              </div>
              <span>CVM</span>
            </div>
            <div className={styles.navItem} onClick={() => window.open('https://www.b3.com.br/pt_br/para-voce', '_blank')}>
              <div className={styles.icon}>
                <AiOutlineBank />
              </div>
              <span>B3</span>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Sidebar;
