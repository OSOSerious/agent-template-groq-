<!-- Sidebar.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  export let activeView: string = 'home';

  const menuItems = [
    { id: 'home', label: 'Home', icon: '🏠' },
    { id: 'templates', label: 'Templates', icon: '📄' },
    { id: 'my-agents', label: 'My Agents', icon: '🤖' },
    { id: 'help', label: 'Help', icon: '❓' },
    { id: 'settings', label: 'Settings', icon: '⚙️' }
  ];

  function handleNavigate(view: string) {
    activeView = view;
    dispatch('navigate', { view });
  }

  function handleNewAgent() {
    dispatch('newAgent');
  }
</script>

<aside class="w-64 bg-gray-800 border-r border-gray-700 flex flex-col">
  <div class="p-4 border-b border-gray-700">
    <h1 class="text-xl font-bold text-white">Agent Console</h1>
    <p class="text-sm text-gray-400">Create & manage your AI agents</p>
  </div>
  
  <nav class="flex-1 p-4">
    {#each menuItems as item}
      <button
        class="block px-4 py-2 rounded text-gray-300 hover:bg-gray-700 hover:text-white transition-colors {activeView === item.id ? 'bg-gray-700 text-white' : ''}"
        on:click={() => handleNavigate(item.id)}
      >
        <span class="text-lg">{item.icon}</span>
        <span>{item.label}</span>
      </button>
    {/each}

    <button
      class="w-full px-4 py-2 mt-4 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
      on:click={handleNewAgent}
    >
      <span>+</span>
      <span>New Agent</span>
    </button>
  </nav>

  <div class="p-4 border-t border-gray-700">
    <button
      class="w-full px-4 py-2 bg-orange-500 text-white rounded hover:bg-orange-600 transition-colors"
    >
      <span>⭐</span>
      <span>Subscribe</span>
    </button>
  </div>
</aside>

<style>
  :global(body) {
    background-color: #111827;
    color: white;
  }
</style>
