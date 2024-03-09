function shuffleArray(array) {
  const shuffledArray = [...array];
  for (let i = shuffledArray.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
  }
  return shuffledArray;
}

const questionsData = [
  {
    question: "What does 'दादा' (Dada) mean in Hindi?",
    options: [
      { answerText: "Brother", isCorrect: false },
      { answerText: "Grandfather", isCorrect: true },
      { answerText: "Uncle", isCorrect: false },
      { answerText: "Father", isCorrect: false },
    ],
  },
  {
    question: "In Hindi, what is the word for 'vegetables'?",
    options: [
      { answerText: "दाल (Daal)", isCorrect: false },
      { answerText: "फल (Phal)", isCorrect: false },
      { answerText: "सब्ज़ी (Sabzi)", isCorrect: true },
      { answerText: "मिठाई (Mithai)", isCorrect: false },
    ],
  },
  {
    question: "What is the Hindi word for 'Tuesday'?",
    options: [
      { answerText: "मंगलवार (Mangalvaar)", isCorrect: true },
      { answerText: "बुधवार (Budhvaar)", isCorrect: false },
      { answerText: "मंगल (Mangal)", isCorrect: false },
      { answerText: "शुक्रवार (Shukravaar)", isCorrect: false },
    ],
  },
  {
    question:
      "Choose the correct form of the verb: 'मैं बहुत अच्छा गाना _____' (gaana - to sing).",
    options: [
      { answerText: "गाता हूँ (gaata hoon)", isCorrect: true },
      { answerText: "गाती हूँ (gaati hoon)", isCorrect: false },
      { answerText: "गाते हैं (gaate hain)", isCorrect: false },
      { answerText: "गाती है (gaati hai)", isCorrect: false },
    ],
  },
  {
    question: "What is the Hindi word for 'morning'?",
    options: [
      { answerText: "शाम (Shaam)", isCorrect: false },
      { answerText: "दोपहर (Dopahar)", isCorrect: false },
      { answerText: "सुबह (Subah)", isCorrect: true },
      { answerText: "रात (Raat)", isCorrect: false },
    ],
  },
];

const root = document.getElementById("root");

function handleAnswerButtonClick(isCorrect) {
  if (isCorrect) {
    score++;
  }

  const nextQuestion = currentQuestion + 1;
  if (nextQuestion < shuffledQuestions.length) {
    setCurrentQuestion(nextQuestion);
  } else {
    setShowScore(true);
  }
}

function restartQuiz() {
  setCurrentQuestion(0);
  setScore(0);
  setShowScore(false);
  setShuffledQuestions(shuffleArray(questionsData));
}

let currentQuestion = 0;
let score = 0;
let showScore = false;
let shuffledQuestions = shuffleArray(questionsData);

function setCurrentQuestion(nextQuestion) {
  currentQuestion = nextQuestion;
  render();
}

function setScore(newScore) {
  score = newScore;
  render();
}

function setShowScore(flag) {
  showScore = flag;
  render();
}

function render() {
  if (showScore) {
    root.innerHTML = `
      <div class="score-section">
        <h1>You've earned ${score} out of ${shuffledQuestions.length} knowledge points!</h1>
        <button onclick="restartQuiz()">Retry</button>
      </div>
    `;
  } else {
    root.innerHTML = `
      <div class="question-section">
        <h1>Question ${currentQuestion + 1}/${shuffledQuestions.length}</h1>
        <div class="question-text">${
          shuffledQuestions[currentQuestion].question
        }</div>
        <div class="options">
          ${shuffledQuestions[currentQuestion].options
            .map(
              (option, index) => `
                <button onclick="handleAnswerButtonClick(${option.isCorrect})">
                  ${option.answerText}
                </button>
              `
            )
            .join("")}
        </div>
      </div>
    `;
  }
}

render();
