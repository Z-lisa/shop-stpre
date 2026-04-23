<template>
  <div class="h-screen flex flex-col bg-gray-50 pb-14">
    <div class="bg-primary px-4 py-3">
      <h1 class="text-white text-lg font-bold">商品分类</h1>
    </div>
    
    <div class="flex-1 flex overflow-hidden">
      <div class="category-menu w-24 bg-white overflow-y-auto flex-shrink-0">
        <div 
          v-for="category in categories" 
          :key="category.id"
          class="menu-item px-2 py-4 text-center border-l-3 transition-colors"
          :class="activeCategory === category.id ? 'bg-gray-50 border-primary text-primary' : 'text-gray-600'"
          @click="selectCategory(category.id)"
        >
          <span class="text-xl block mb-1">{{ category.icon }}</span>
          <span class="text-xs">{{ category.name }}</span>
        </div>
      </div>
      
      <div class="flex-1 overflow-y-auto p-4">
        <h2 class="text-base font-bold text-gray-800 mb-4">{{ categoryName }}</h2>
        <div class="product-grid grid grid-cols-2 gap-3">
          <div 
            v-for="product in categoryProducts" 
            :key="product.id"
            class="product-card bg-white rounded-lg p-2 shadow-sm"
            @click="goToDetail(product.id)"
          >
            <img :src="product.cover" :alt="product.name" class="w-full h-36 object-cover rounded" />
            <p class="text-sm text-gray-800 mt-2 truncate">{{ product.name }}</p>
            <p class="text-xs text-gray-500 truncate mt-1">{{ product.author }}</p>
            <div class="flex items-center justify-between mt-2">
              <span class="text-sm text-primary font-bold">¥{{ product.price }}</span>
              <span class="text-xs text-gray-400">{{ product.rating }}分</span>
            </div>
          </div>
        </div>
        
        <div v-if="categoryProducts.length === 0" class="text-center py-10 text-gray-400">
          暂无商品
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { categories, getProductsByCategory } from '../data/books'

const router = useRouter()
const route = useRoute()
const activeCategory = ref(1)

const categoryName = computed(() => {
  const category = categories.find(c => c.id === activeCategory.value)
  return category ? category.name : ''
})

const categoryProducts = computed(() => {
  return getProductsByCategory(activeCategory.value)
})

const selectCategory = (categoryId) => {
  activeCategory.value = categoryId
}

const goToDetail = (bookId) => {
  router.push(`/book/${bookId}`)
}

onMounted(() => {
  if (route.query.id) {
    activeCategory.value = parseInt(route.query.id)
  }
})

watch(() => route.query.id, (newId) => {
  if (newId) {
    activeCategory.value = parseInt(newId)
  }
})
</script>

<style scoped>
.border-l-3 {
  border-left-width: 3px;
}

.category-menu::-webkit-scrollbar {
  width: 0;
}
</style>
