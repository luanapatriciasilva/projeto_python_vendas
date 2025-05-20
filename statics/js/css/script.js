document.addEventListener('DOMContentLoaded', () => {
    const filterForm = document.getElementById('filter-form');
    if (filterForm) {
        filterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const category = document.getElementById('category').value;
            const minPrice = document.getElementById('min_price').value;
            const maxPrice = document.getElementById('max_price').value;
            window.location.href = `/?category=${category}&min_price=${minPrice}&max_price=${maxPrice}`;
        });
    }
});