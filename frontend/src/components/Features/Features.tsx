import { FeatureCard } from "./FeatureCard";
import styles from "./Features.module.css";

const features = [
    { icon: '🚀', title: 'Rendimiento', description: 'Optimizado para la máxima velocidad y latencia mínima.' },
    { icon: '🔒', title: 'Seguridad', description: 'Protección de datos y autenticación robusta por defecto.' },
    { icon: '⚡', title: 'Escalabilidad', description: 'Crece sin fricciones desde prototipos hasta millones de usuarios.' },
    { icon: '🛠️', title: 'Fácil Integración', description: 'APIs y herramientas listas para conectar con tu flujo actual.' },
    { icon: '📊', title: 'Métricas en Vivo', description: 'Monitoreo y observabilidad en tiempo real de tu sistema.' },
    { icon: '🤝', title: 'Colaboración', description: 'Diseñado para que los equipos coordinen tareas eficientemente.' },
];

export const Features = () => {
    return (
                <section id="features" className={styles.featuresSection}>
                    <div className={styles.header}>
                        <h2>Características</h2>
                        <p>Herramientas modernas para equipos ambiciosos. Lanza más rápido y escala sin preocuparte por la infraestructura.</p>
                    </div>
                    <div className={styles.grid}>
                        {features.map((feature) => (
                            <FeatureCard
                                key={feature.title}
                                icon={feature.icon}
                                title={feature.title}
                                description={feature.description}
                            />
                        ))}
                    </div>
                </section>
                );
};

                export default Features;