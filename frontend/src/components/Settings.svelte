<script lang="ts">
  import { writable } from 'svelte/store';

  const settings = writable({
    darkMode: true,
    temperature: 0.7,
    maxTokens: 1024,
    model: 'mixtral-8x7b-32768'
  });

  let currentSettings;
  settings.subscribe(value => {
    currentSettings = value;
  });

  function handleSave() {
    settings.set(currentSettings);
    // TODO: Implement settings persistence
  }
</script>

<div class="p-6 max-w-2xl mx-auto">
  <h2 class="text-2xl font-bold mb-6 text-white">Settings</h2>
  
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <label class="text-white">Dark Mode</label>
      <input
        type="checkbox"
        bind:checked={currentSettings.darkMode}
        class="toggle"
      />
    </div>

    <div>
      <label class="text-white block mb-2">Temperature</label>
      <input
        type="range"
        min="0"
        max="1"
        step="0.1"
        bind:value={currentSettings.temperature}
        class="w-full"
      />
      <span class="text-gray-400">{currentSettings.temperature}</span>
    </div>

    <div>
      <label class="text-white block mb-2">Max Tokens</label>
      <input
        type="number"
        bind:value={currentSettings.maxTokens}
        class="w-full bg-gray-800 text-white rounded p-2"
      />
    </div>

    <div>
      <label class="text-white block mb-2">Model</label>
      <select
        bind:value={currentSettings.model}
        class="w-full bg-gray-800 text-white rounded p-2"
      >
        <option value="mixtral-8x7b-32768">Mixtral 8x7B</option>
        <option value="llama-3.3-70b-versatile">Llama 3.3 70B</option>
      </select>
    </div>

    <button
      on:click={handleSave}
      class="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition-colors"
    >
      Save Settings
    </button>
  </div>
</div>

<style>
  .toggle {
    @apply appearance-none w-12 h-6 rounded-full bg-gray-300 checked:bg-blue-600 transition-colors duration-200 relative cursor-pointer;
  }
  
  .toggle:before {
    content: '';
    @apply absolute w-4 h-4 bg-white rounded-full left-1 top-1 transition-transform duration-200;
  }
  
  .toggle:checked:before {
    @apply transform translate-x-6;
  }
</style>
