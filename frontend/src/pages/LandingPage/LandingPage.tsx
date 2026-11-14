import { Banner } from "../../components/Banner/Banner"
import { ContactForm } from "../../components/ContactForm/ContactForm"
import { Features } from "../../components/Features/Features"
import { Footer } from "../../components/Footer/Footer"
import { Navbar } from "../../components/Navbar/Navbar"

export const LandingPage = () => {
    return (
        <>
            <Navbar />
            <main>
                <Banner />
                <Features />
                <ContactForm />
            </main>
            <Footer />
        </>
    )
}