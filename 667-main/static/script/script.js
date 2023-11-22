const advices = [
  "Embrace Change: Life is constantly evolving; learn to adapt and grow through its transitions. Embracing change allows for personal development and new opportunities.",
"Prioritize Self-Care: Take care of your physical, mental, and emotional well-being. Prioritizing self-care enables you to function at your best and maintain balance in life.",
"Practice Gratitude: Cultivate thankfulness for what you have; it brings positivity and contentment. Acknowledging gratitude promotes a healthier mindset and appreciation for life's blessings.",
"Keep Learning: Pursue knowledge continuously; it keeps your mind active and expands your horizons. Lifelong learning fosters personal growth and adaptability.",
"Set Boundaries: Establish healthy limits to safeguard your time and energy; it's essential for your well-being. Setting boundaries ensures respect for your needs and priorities.",
"Value Relationships: Invest in meaningful connections with friends, family, and loved ones. Nurturing relationships brings support, happiness, and a sense of belonging.",
"Embrace Failure: See failure as a stepping stone to success; it offers lessons and growth opportunities. Embracing failure builds resilience and determination.",
"Be Kind: Practice kindness and empathy towards yourself and others. Small acts of kindness can make a significant impact on people's lives.",
"Stay Present: Focus on the present moment to reduce stress and anxiety. Practicing mindfulness enhances awareness and appreciation for life.",
"Take Risks: Don't be afraid to take calculated risks; they often lead to new discoveries and personal growth. Taking risks can open doors to unexpected opportunities.",
"Follow Your Passions: Pursue activities and interests that ignite your enthusiasm. Following your passions brings fulfillment and purpose to life.",
"Be Flexible: Adaptability is key in life; stay open to change and be willing to adjust. Being flexible allows for smoother navigation through challenges.",
"Practice Resilience: Develop the ability to bounce back from setbacks. Resilience strengthens your capacity to overcome obstacles and adversity.",
"Value Time: Time is a valuable resource; use it wisely on things that matter most. Managing time effectively enhances productivity and satisfaction.",
"Be Authentic: Stay true to your values, beliefs, and personality. Authenticity fosters genuine connections and self-acceptance.",
"Seek Balance: Maintain a balance between work, personal life, and relaxation. Balancing priorities promotes overall well-being and prevents burnout.",
"Keep an Open Mind: Be receptive to new ideas, perspectives, and experiences. Open-mindedness encourages personal growth and understanding.",
"Forgive and Let Go: Release resentment and forgive others to find peace within yourself. Letting go of grudges frees you from negativity.",
"Celebrate Small Wins: Acknowledge and celebrate your achievements, no matter how small. Celebrating successes boosts motivation and confidence.",
"Enjoy the Journey: Life is a journey full of experiences; cherish every moment and embrace the lessons it offers. Enjoying the journey makes life more fulfilling and meaningful."
];

function getRandomAdvice() {
  const randomIndex = Math.floor(Math.random() * advices.length);
  return randomIndex;
}

// Получаем элемент, в котором будет отображаться совет
const adviceElement = document.getElementById('advice');

// При загрузке страницы выводим первый случайный совет
let sum = getRandomAdvice()
adviceElement.textContent = advices[sum];
// Чтобы менять совет при каждом обновлении страницы, раскомментируйте следующую строку
// setInterval(() => { adviceElement.textContent = getRandomAdvice(); }, 5000); // Изменяет совет каждые 5 секунд
