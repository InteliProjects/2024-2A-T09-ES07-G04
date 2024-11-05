import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import styles from './Loader.module.css';

export default function Loader() {
    return (
        <div className={styles.bg}>
            <Box sx={{ display: 'flex' }}>
                <CircularProgress style={{color: 'white'}}/>
            </Box>
        </div>
    );
}