import React from 'react';

// Using ES6 Arrow Function syntax for our React Component
const HomePage = () => {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-5xl font-bold text-blue-400">
        Forge 
      </h1>
      <p className="mt-4 text-xl text-gray-400">
        The AI-Powered Engineering Workspace
      </p>
    </main>
  );
};

export default HomePage;