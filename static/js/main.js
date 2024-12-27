document.addEventListener('DOMContentLoaded', function() {
    // Handle delete contact
    const deleteButtons = document.querySelectorAll('.delete-contact');
    const deleteModal = document.getElementById('deleteModal');
    const confirmDeleteBtn = document.getElementById('confirmDelete');
    let contactToDelete = null;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            contactToDelete = this.dataset.id;
            const modal = new bootstrap.Modal(deleteModal);
            modal.show();
        });
    });

    confirmDeleteBtn.addEventListener('click', function() {
        if (contactToDelete) {
            window.location.href = `/delete_contact/${contactToDelete}`;
        }
    });

    // Handle favorite toggle
    const favoriteButtons = document.querySelectorAll('.favorite-btn');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const contactId = this.dataset.id;
            const icon = this.querySelector('i');

            fetch(`/toggle_favorite/${contactId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        if (data.favorite) {
                            icon.classList.remove('bi-star');
                            icon.classList.add('bi-star-fill', 'text-warning');
                        } else {
                            icon.classList.remove('bi-star-fill', 'text-warning');
                            icon.classList.add('bi-star');
                        }
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
});
