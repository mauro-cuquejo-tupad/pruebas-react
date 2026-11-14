import styles from "./Footer.module.css";

export const Footer = () => {
    return (
        <footer className={styles.footer}>
            <div className={styles.container}>
                <p className={styles.text}>© 2026 TODO MIO Y SOLO MIO S.R.L. Todos los derechos reservados.</p>
                <div className={styles.links}>
                    <a href="#features" className={styles.link}>Características</a>
                    <a href="#contact" className={styles.link}>Contacto</a>
                    <a href="#" className={styles.link}>Privacidad</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
