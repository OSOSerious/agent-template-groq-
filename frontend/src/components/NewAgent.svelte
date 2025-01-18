<script lang="ts">
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  let agentName = '';
  let description = '';
  let systemPrompt = '';
  let icon = '🤖';

  const icons = ['🤖', '🧠', '📚', '✈️', '🎮', '📝', '🎨', '🔬', '💼', '🌍'];

  function handleSubmit() {
    const newAgent = {
      name: agentName,
      description,
      system_prompt: systemPrompt,
      icon
    };

    dispatch('create', newAgent);
    
    // Reset form
    agentName = '';
    description = '';
    systemPrompt = '';
    icon = '🤖';
  }
</script>

<div class="p-6 max-w-2xl mx-auto">
  <h2 class="text-2xl font-bold mb-6 text-white">Create New Agent</h2>
  
  <form on:submit|preventDefault={handleSubmit} class="space-y-6">
    <div>
      <label class="text-white block mb-2">Agent Name</label>
      <input
        type="text"
        bind:value={agentName}
        required
        class="w-full bg-gray-800 text-white rounded p-2"
        placeholder="e.g., Research Assistant"
      />
    </div>

    <div>
      <label class="text-white block mb-2">Description</label>
      <textarea
        bind:value={description}
        required
        class="w-full bg-gray-800 text-white rounded p-2 h-24"
        placeholder="Describe what your agent does..."
      ></textarea>
    </div>

    <div>
      <label class="text-white block mb-2">System Prompt</label>
      <textarea
        bind:value={systemPrompt}
        required
        class="w-full bg-gray-800 text-white rounded p-2 h-48"
        placeholder="Define your agent's behavior and capabilities..."
      ></textarea>
    </div>

    <div>
      <label class="text-white block mb-2">Icon</label>
      <div class="flex flex-wrap gap-2">
        {#each icons as iconOption}
          <button
            type="button"
            class="w-10 h-10 rounded {icon === iconOption ? 'bg-blue-600' : 'bg-gray-800'} hover:bg-blue-500 transition-colors"
            on:click={() => icon = iconOption}
          >
            {iconOption}
          </button>
        {/each}
      </div>
    </div>

    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition-colors"
    >
      Create Agent
    </button>
  </form>
</div>
