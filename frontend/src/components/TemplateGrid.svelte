<!-- TemplateGrid.svelte -->
<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { Template } from '../types';

  const dispatch = createEventDispatcher();

  export let templates: Template[] = [
    {
      id: 'ResearchGPT',
      name: 'ResearchGPT',
      description: 'Generate a thorough report on a specific subject',
      icon: '📚'
    },
    {
      id: 'TravelGPT',
      name: 'TravelGPT',
      description: 'Plan a detailed journey to a selected destination',
      icon: '✈️'
    },
    {
      id: 'StudyGPT',
      name: 'StudyGPT',
      description: 'Design a study plan for a selected topic',
      icon: '📝'
    },
    {
      id: 'BrandGPT',
      name: 'BrandGPT',
      description: 'Create a brand persona, market position, and future prospects',
      icon: '🎯'
    },
    {
      id: 'IndustryGPT',
      name: 'IndustryGPT',
      description: 'Analyze trends and behaviors of an industry, covering key trends, players, and future predictions',
      icon: '🏭'
    },
    {
      id: 'ResumeGPT',
      name: 'ResumeGPT',
      description: 'Design a professional resume based on your career history and skills',
      icon: '📄'
    },
    {
      id: 'MarketingGPT',
      name: 'MarketingGPT',
      description: 'Design a comprehensive marketing strategy for your business',
      icon: '📢'
    },
    {
      id: 'BudgetGPT',
      name: 'BudgetGPT',
      description: 'Prepare a personal or family budget',
      icon: '💰'
    },
    {
      id: 'StudyGPT',
      name: 'StudyGPT',
      description: 'Design a study schedule to achieve your academic objectives',
      icon: '📚'
    }
  ];

  let searchQuery = '';

  $: filteredTemplates = templates.filter(template =>
    template.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    template.description.toLowerCase().includes(searchQuery.toLowerCase())
  );

  function handleTemplateClick(template: Template) {
    dispatch('select', template);
  }
</script>

<div class="p-6">
  <div class="mb-6">
    <input
      type="text"
      bind:value={searchQuery}
      placeholder="Search templates..."
      class="w-full p-2 rounded bg-gray-800 border border-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
    />
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    {#each filteredTemplates as template}
      <button
        class="p-4 rounded-lg bg-gray-800 hover:bg-gray-700 transition-colors text-left border border-gray-700"
        on:click={() => handleTemplateClick(template)}
      >
        <div class="flex items-center space-x-2 mb-2">
          <span class="text-2xl">{template.icon}</span>
          <span class="font-semibold">{template.name}</span>
        </div>
        <p class="text-sm text-gray-400">{template.description}</p>
      </button>
    {/each}
  </div>
</div>

<style>
  :global(body) {
    @apply bg-gray-900;
  }
</style>
