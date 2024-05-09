document.addEventListener('DOMContentLoaded', function() {
    const transactionForm = document.getElementById('transactionForm');
    const blockchainDiv = document.getElementById('blockchain');
    const lastBlockDiv = document.getElementById('lastBlock');
    const mineButton = document.getElementById('mineButton');

    // Function to fetch and display the blockchain
    function fetchBlockchain() {
        fetch('/chain')
            .then(response => response.json())
            .then(data => {
                blockchainDiv.innerHTML = '<h3>Blockchain</h3>';
                data.chain.forEach(block => {
                    const blockDiv = document.createElement('div');
                    blockDiv.innerHTML = `
                        <strong>Index:</strong> ${block.index}<br>
                        <strong>Timestamp:</strong> ${new Date(block.timestamp * 1000).toLocaleString()}<br>
                        <strong>Transactions:</strong> ${block.transactions.length}<br>
                        <strong>Proof:</strong> ${block.proof}<br>
                        <strong>Previous Hash:</strong> ${block.previous_hash}<br><br>
                    `;
                    blockchainDiv.appendChild(blockDiv);
                });
            });
    }

    // Function to fetch and display the last block
    function fetchLastBlock() {
        fetch('/chain')
            .then(response => response.json())
            .then(data => {
                const lastBlock = data.chain[data.chain.length - 1];
                lastBlockDiv.innerHTML = '<h3>Last Block</h3>';
                lastBlockDiv.innerHTML += `
                    <strong>Index:</strong> ${lastBlock.index}<br>
                    <strong>Timestamp:</strong> ${new Date(lastBlock.timestamp * 1000).toLocaleString()}<br>
                    <strong>Transactions:</strong> ${lastBlock.transactions.length}<br>
                    <strong>Proof:</strong> ${lastBlock.proof}<br>
                    <strong>Previous Hash:</strong> ${lastBlock.previous_hash}<br><br>
                `;
            });
    }

    // Function to handle form submission
    transactionForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(transactionForm);
        const sender = formData.get('sender');
        const recipient = formData.get('recipient');
        const amount = formData.get('amount');

        fetch('/transactions/new', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({sender, recipient, amount})
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert(data.message);
        });
    });

    // Function to handle mining button click
    mineButton.addEventListener('click', function() {
        fetch('/mine')
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert(data.message);
            });
    });

    // Initial fetches to populate the blockchain and last block
    fetchBlockchain();
    fetchLastBlock();
});
