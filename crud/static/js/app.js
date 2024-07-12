document.addEventListener('DOMContentLoaded', function () {
    var recordModalElement = document.getElementById('recordModal');

    if (!recordModalElement) return;

    recordModalElement.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget; // Button that triggered the modal
        var recordId = button.getAttribute('data-record-id');
        var firstName = button.getAttribute('data-record-first-name');
        var lastName = button.getAttribute('data-record-last-name');
        var email = button.getAttribute('data-record-email');
        var phone = button.getAttribute('data-record-phone');
        var address = button.getAttribute('data-record-address');
        var city = button.getAttribute('data-record-city');
        var cgpa = button.getAttribute('data-record-cgpa');
        var achievement = button.getAttribute('data-record-achievement');
        var internship = button.getAttribute('data-record-internship');
        var placement = button.getAttribute('data-record-placement');
        var higherStudies = button.getAttribute('data-record-higher-studies');
        var entreprenuership = button.getAttribute('data-record-entreprenuership');
        var extraCurricular = button.getAttribute('data-record-extra-curricular');
        var publications = button.getAttribute('data-record-publications');
        var practiseSchool = button.getAttribute('data-record-practise-school');
        var conference = button.getAttribute('data-record-conference');

        var modalBody = recordModalElement.querySelector('.modal-body');
        modalBody.innerHTML = `
                <p><strong>ID:</strong> ${recordId}</p>
                <p><strong>First Name:</strong> ${firstName}</p>
                <p><strong>Last Name:</strong> ${lastName}</p>
                <p><strong>Email:</strong> ${email}</p>
                <p><strong>Phone:</strong> ${phone}</p>
                <p><strong>Address:</strong> ${address}</p>
                <p><strong>City:</strong> ${city}</p>
                <p><strong>CGPA:</strong> ${cgpa}</p>
                <p><strong>Achievement:</strong> <a href="${achievement}" target="_blank">${achievement}</a></p>
                <p><strong>Internship:</strong> <a href="${internship}" target="_blank">${internship}</a></p>
                <p><strong>Placement:</strong> <a href="${placement}" target="_blank">${placement}</a></p>
                <p><strong>Higher Studies:</strong> <a href="${higherStudies}" target="_blank">${higherStudies}</a></p>
                <p><strong>Entreprenuership:</strong> <a href="${entreprenuership}" target="_blank">${entreprenuership}</a></p>
                <p><strong>Extra Curricular:</strong> <a href="${extraCurricular}" target="_blank">${extraCurricular}</a></p>
                <p><strong>Publications:</strong> <a href="${publications}" target="_blank">${publications}</a></p>
                <p><strong>Practise School:</strong> <a href="${practiseSchool}" target="_blank">${practiseSchool}</a></p>
                <p><strong>Conference:</strong> <a href="${conference}" target="_blank">${conference}</a></p>
            `;
    });
});