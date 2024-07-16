
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    let isSliding = false;

    function showSlide(index) {
        const slider = document.querySelector('.slider');
        slider.style.transform = `translateX(${-index * 100}%)`;
    }

    function nextSlide() {
        if (isSliding) return;
        isSliding = true;
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
        setTimeout(() => isSliding = false, 1000); // Adjust to match CSS transition duration
    }

    function prevSlide() {
        if (isSliding) return;
        isSliding = true;
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
        setTimeout(() => isSliding = false, 1000); // Adjust to match CSS transition duration
    }

    // Auto slide function
    setInterval(nextSlide, 5000); // Change slide every 5 seconds

    // Add event listeners for manual slide control
    document.querySelector('.next-slide').addEventListener('click', nextSlide);
    document.querySelector('.prev-slide').addEventListener('click', prevSlide);

    // Ensure initial slide is shown
    showSlide(currentSlide);

