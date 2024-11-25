let currentQuestion = 1;

// Carrega as perguntas do back-end e cria o HTML dinamicamente
async function loadQuestions() {
    try {
        const response = await fetch('/my_app/api/questions/');
        const data = await response.json();

        const questionsContainer = document.getElementById('questionsContainer');

        // Para cada pergunta recebida, cria o HTML dinâmico
        data.questions.forEach((question, index) => {
            const questionDiv = document.createElement('div');
            questionDiv.classList.add('question-page');
            questionDiv.id = `question${question.id}`;
            if (index !== 0) questionDiv.classList.add('hidden'); // Esconde todas as perguntas, exceto a primeira

            // Título da pergunta
            const questionTitle = document.createElement('div');
            questionTitle.classList.add('question');
            questionTitle.textContent = question.text;
            questionDiv.appendChild(questionTitle);

            // Opções de resposta
            const optionsDiv = document.createElement('div');
            optionsDiv.classList.add('options');
            question.choices.forEach(choice => {
                const optionButton = document.createElement('button');
                optionButton.classList.add('option-btn');
                optionButton.dataset.value = choice.value;
                optionButton.textContent = choice.text;
                
                // Evento para marcar a opção como selecionada
                optionButton.addEventListener('click', function () {
                    optionsDiv.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
                    optionButton.classList.add('selected');
                });

                optionsDiv.appendChild(optionButton);
            });

            questionDiv.appendChild(optionsDiv);

            // Botão para enviar e ir para a próxima pergunta
            const submitButton = document.createElement('button');
            submitButton.classList.add('submit-btn');
            submitButton.textContent = 'Enviar';
            submitButton.onclick = () => {
                if (index < data.questions.length - 1) {
                    nextQuestion(index + 2); // Vai para a próxima pergunta
                } else {
                    finalFeedback(); // Exibe o feedback final se for a última pergunta
                }
            };
            questionDiv.appendChild(submitButton);

            questionsContainer.appendChild(questionDiv);
        });
    } catch (error) {
        console.error('Erro ao carregar perguntas:', error);
    }
}


function nextQuestion(nextPage) {
    // Esconde a pergunta atual
    document.getElementById('question' + currentQuestion).classList.add('hidden');
    // Mostra a próxima pergunta
    currentQuestion = nextPage;
    document.getElementById('question' + currentQuestion).classList.remove('hidden');
}

function showFeedback() {
    // Esconde a última pergunta e mostra a página de feedback
    document.getElementById('question' + currentQuestion).classList.add('hidden');
    document.getElementById('feedbackPage').classList.remove('hidden');
}

// Inicia o carregamento das perguntas quando a página é carregada
window.onload = loadQuestions;
