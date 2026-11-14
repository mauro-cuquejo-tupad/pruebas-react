import styles from "./ContactForm.module.css";

export const ContactForm = () => {
    return (
        <section id="contact" className={styles.contactSection}>
            <div className={styles.container}>
                <div className={styles.infoCol}>
                    <h4 className={styles.tagline}>
                        <span>//</span> ¡Hablemos!
                    </h4>
                    <h2 className={styles.title}>
                        Hablemos de tu proyecto
                    </h2>
                    <p className={styles.description}>
                        Siéntete libre de contactarme para discutir posibles colaboraciones, proyectos o
                        simplemente para decir hola. Estoy abierto a nuevas oportunidades y me encanta
                        conocer gente nueva.
                    </p>
                    <div className={styles.contactDetails}>
                        <span className={styles.contactItem}>
                            <span className={styles.contactItemIcon}>✉</span> mauro.cuquejo@tupad.utn.edu.ar
                        </span>
                        <span className={styles.contactItem}>
                            <span className={styles.contactItemIcon}>📞</span> +54 9 11 5628 2192
                        </span>
                        <span className={styles.contactItem}>
                            <span className={styles.contactItemIcon}>📍</span> Buenos Aires, Argentina
                        </span>
                    </div>
                    <div className={styles.socialLinks}>
                        <a href="https://github.com" target="_blank" rel="noreferrer" className={styles.socialBtn} aria-label="GitHub" title="GitHub">
                            GH
                        </a>
                        <a href="https://linkedin.com" target="_blank" rel="noreferrer" className={styles.socialBtn} aria-label="LinkedIn" title="LinkedIn">
                            IN
                        </a>
                        <a href="https://instagram.com" target="_blank" rel="noreferrer" className={styles.socialBtn} aria-label="Instagram" title="Instagram">
                            IG
                        </a>
                    </div>
                </div>

                <form className={styles.form} onSubmit={(e) => e.preventDefault()}>
                    <div className={styles.row}>
                        <div className={styles.fieldGroup}>
                            <label className={styles.label} htmlFor="name">Nombre</label>
                            <input className={styles.input} type="text" id="name" required placeholder="Tu nombre" />
                        </div>
                        <div className={styles.fieldGroup}>
                            <label className={styles.label} htmlFor="email">Correo electrónico</label>
                            <input className={styles.input} type="email" id="email" required placeholder="ejemplo@correo.com" />
                        </div>
                    </div>
                    <div className={styles.fieldGroup}>
                        <label className={styles.label} htmlFor="message">Mensaje</label>
                        <textarea className={styles.textarea} id="message" required placeholder="Cuéntame sobre tu proyecto o consulta..."></textarea>
                    </div>
                    <button type="submit" className={styles.submitBtn}>
                        Enviar mensaje
                    </button>
                </form>
            </div>
        </section>
    );
};

export default ContactForm;
