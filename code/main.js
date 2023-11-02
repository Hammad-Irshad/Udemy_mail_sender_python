const nodeMailer = require('nodemailer');
const fs = require('fs');

let links = []; // Initialize an empty array to store links
let lines = []; // Initialize an empty array to store lines
let temp = [];

const maillist = [
    'hammadirshad300@gmail.com',
    'hammadirshad23@gmail.com',
    'iqna2018@gmail.com',
];

// Read the contents of text.txt
fs.readFile('code/text.txt', 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }

    fs.readFile('code/temp.txt', 'utf8', (err, word) => {
        if (err) {
            console.error("Error reading file:", err);
            return;
        }

        temp = word.split('\n');
        // Split the file content into an array of lines
        lines = data.split('\n');

        // Iterate through the lines
        lines.forEach(line => {
            if (line.includes('php') || line.includes('python') || line.includes('google') || line.includes('aws') || line.includes('azure')
            || line.includes('scrap') || line.includes('bootcamp') || line.includes('js') || line.includes('language') || line.includes('microsoft')
            || line.includes('learn') || line.includes('react') || line.includes('gcp') || line.includes('project') || line.includes('learning')
            ) {
                links.push(line.trim()); // Trim to remove any extra spaces
            }
        });

        // If there are links, send an email
        if (temp.join() !== lines.join()) {
            sendEmail(links, lines);
        }
        

        fs.writeFile('code/temp.txt', lines.join('\n'), 'utf8', (err) => {
            if (err) {
                console.error("Error writing to file:", err);
            } else {
                console.log("Data written to file successfully.");
            }
        });
    });
});

function sendEmail(links, lines) {
    const linesList = lines.map(line => `<li>${line}</li>`).join('');
    const linksList = links.map(link => `<li>${link}</li>`).join('');

    const html = `
        <h2>All Links:</h2>
        <ul>${linesList}</ul>

        <h2>Interested Links:</h2>
        <ul>${linksList}</ul>
    `;

    const transporter = nodeMailer.createTransport({
        host: "smtp.office365.com",
        port: 587,
        secure: false,
        auth: {
            user: "hammadirshad305@outlook.com",
            pass: "tgyfajllloxuuuim",
        },
    });

    transporter.sendMail({
        from: 'hammad irshad <hammadirshad305@outlook.com>',
        to: maillist,
        subject: 'Udemy coupon sender',
        html: html,
    }, (error, info) => {
        if (error) {
            console.error("Error sending email:", error);
        } else {
            console.log("Message sent:", info.messageId);
        }
    });
}
