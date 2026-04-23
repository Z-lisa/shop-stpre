<template>
  <div class="min-h-screen bg-gray-50 pb-16">
    <div class="bg-primary px-4 py-3">
      <div class="flex items-center gap-2">
        <div class="flex-1 relative">
          <input
            v-model="searchKeyword"
            type="text"
            placeholder="搜索商品名称/品牌"
            class="w-full h-10 pl-10 pr-4 rounded-lg bg-white text-sm"
            @keyup.enter="handleSearch"
          />
          <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
        <button class="text-white px-3" @click="goBack">取消</button>
      </div>
    </div>

    <div class="px-4 py-3">
      <p class="text-sm text-gray-500">
        搜索: <span class="text-gray-800">"{{ keyword }}"</span>
        <span class="ml-2">找到 {{ searchResults.length }} 件商品</span>
      </p>
    </div>

    <div v-if="searchResults.length > 0" class="search-results px-4">
      <div 
        v-for="product in searchResults" 
        :key="product.id"
        class="result-item bg-white rounded-lg p-3 mb-3 flex gap-3 shadow-sm"
        @click="goToDetail(product.id)"
      >
        <img :src="product.cover" :alt="product.name" class="w-20 h-24 object-cover rounded flex-shrink-0" />
        <div class="flex-1 min-w-0">
          <h3 class="text-sm font-medium text-gray-800 truncate">{{ product.name }}</h3>
          <p class="text-xs text-gray-500 mt-1 truncate">{{ product.author }}</p>
          <p class="text-xs text-gray-400 mt-1 truncate">{{ product.publisher }}</p>
          <div class="flex items-center justify-between mt-2">
            <span class="text-sm text-primary font-bold">¥{{ product.price }}</span>
            <span class="text-xs text-gray-400">{{ product.rating }}分</span>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="empty-results flex flex-col items-center justify-center py-20">
      <svg class="w-20 h-20 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      <p class="text-gray-400 mt-4">未找到相关商品</p>
      <p class="text-xs text-gray-300 mt-2">试试其他关键词</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProductsByKeyword } from '../data/books'

const route = useRoute()
const router = useRouter()

const keyword = ref('')
const searchKeyword = ref('')

const searchResults = computed(() => {
  if (!keyword.value) return []
  return getProductsByKeyword(keyword.value)
})

const handleSearch = () => {
  if (searchKeyword.value.trim()) {
    keyword.value = searchKeyword.value.trim()
  }
}

const goToDetail = (productId) => {
  router.push(`/book/${productId}`)
}

const goBack = () => {
  router.back()
}

onMounted(() => {
  if (route.query.keyword) {
    keyword.value = route.query.keyword
    searchKeyword.value = route.query.keyword
  }
})

watch(() => route.query.keyword, (newKeyword) => {
  if (newKeyword) {
    keyword.value = newKeyword
    searchKeyword.value = newKeyword
  }
})
</script>
