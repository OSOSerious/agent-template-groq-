<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let agentName = '';
  let goal = '';

  const examples = [
    'Create a comprehensive report of the Nike company',
    'Plan a detailed trip to Hawaii',
    'Create a study plan for a History 101 exam about world events in the 1980s'
  ];

  function handleDeploy() {
    if (agentName && goal) {
      const newAgent = {
        name: agentName,
        description: goal,
        system_prompt: `You are an AI assistant named ${agentName}. Your goal is to: ${goal}`,
        icon: '🤖'
      };

      dispatch('create', newAgent);
      
      // Reset form
      agentName = '';
      goal = '';
    }
  }
</script>

<div class="flex justify-center items-center min-h-screen p-4 sm:p-8">
  <div class="bg-black/80 p-6 sm:p-8 rounded-2xl w-full max-w-3xl text-white">
    <div class="text-center mb-8">
      <h1 class="text-4xl sm:text-5xl font-bold mb-4">AgentGPT</h1>
      <p class="text-gray-300">Create an agent by adding a name / goal, and hitting deploy! Try our examples below!</p>
    </div>

    <div class="space-y-4 mb-8">
      <div>
        <input
          type="text"
          placeholder="Name your agent..."
          bind:value={agentName}
          class="w-full px-4 py-3 bg-transparent border border-white/20 rounded-lg text-white placeholder-gray-400 focus:border-white/50 focus:outline-none transition-colors"
        />
      </div>

      <div>
        <textarea
          placeholder="Describe your agent's goal..."
          bind:value={goal}
          rows="4"
          class="w-full px-4 py-3 bg-transparent border border-white/20 rounded-lg text-white placeholder-gray-400 focus:border-white/50 focus:outline-none transition-colors resize-none"
        ></textarea>
      </div>

      <button
        class="w-full py-3 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed text-white rounded-lg font-medium transition-colors"
        on:click={handleDeploy}
        disabled={!agentName || !goal}
      >
        Deploy Agent
      </button>
    </div>

    <div class="text-center">
      <p class="text-gray-300 mb-4">Example Goals:</p>
      <div class="flex flex-wrap gap-2 justify-center">
        {#each examples as example}
          <button
            class="px-4 py-2 border border-white/20 rounded-lg text-white hover:border-white hover:bg-white/5 transition-colors text-sm"
            on:click={() => goal = example}
          >
            {example}
          </button>
        {/each}
      </div>
    </div>
  </div>
</div>
