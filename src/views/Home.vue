<template>
  <div class="pb-16 bg-gray-50">
    <div class="bg-primary sticky top-0 z-40">
      <div class="px-4 py-3">
        <div class="flex items-center gap-2">
          <div class="flex-1 relative">
            <input
              v-model="searchKeyword"
              type="text"
              placeholder="搜索商品名称/品牌"
              class="w-full h-10 pl-10 pr-4 rounded-lg bg-white text-sm"
              @keyup.enter="handleSearch"
              @focus="showSearchHistory = true"
              @input="handleInput"
            />
            <svg class="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            <button 
              v-if="searchKeyword" 
              class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400"
              @click="searchKeyword = ''"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
        
        <!-- 搜索建议/历史记录 -->
        <div v-if="showSearchHistory" class="absolute left-4 right-4 top-full mt-1 bg-white rounded-lg shadow-lg z-100 max-h-80 overflow-y-auto">
          <!-- 实时搜索结果 -->
          <div v-if="searchKeyword && searchSuggestions.length > 0" class="p-3">
            <p class="text-xs text-gray-400 mb-2">搜索结果</p>
            <div 
              v-for="product in searchSuggestions" 
              :key="product.id"
              class="flex items-center gap-3 p-2 hover:bg-gray-50 rounded cursor-pointer"
              @click="goToDetail(product.id)"
            >
              <img :src="product.cover" class="w-10 h-14 object-cover rounded" />
              <div class="flex-1">
                <p class="text-sm text-gray-800">{{ product.name }}</p>
                <p class="text-xs text-gray-400">{{ product.author }}</p>
              </div>
              <span class="text-sm text-primary font-bold">¥{{ product.price }}</span>
            </div>
          </div>
          
          <!-- 搜索历史 -->
          <div v-else-if="searchHistory.length > 0" class="p-3">
            <div class="flex items-center justify-between mb-2">
              <p class="text-xs text-gray-400">搜索历史</p>
              <button class="text-xs text-gray-400" @click="clearHistory">清空</button>
            </div>
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="(keyword, index) in searchHistory" 
                :key="index"
                class="px-3 py-1.5 bg-gray-100 rounded-full text-sm text-gray-600"
                @click="searchFromHistory(keyword)"
              >
                {{ keyword }}
              </span>
            </div>
          </div>
          
          <!-- 热门搜索 -->
          <div v-else class="p-3">
            <p class="text-xs text-gray-400 mb-2">热门搜索</p>
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="(keyword, index) in hotKeywords" 
                :key="index"
                class="px-3 py-1.5 bg-gray-100 rounded-full text-sm text-gray-600"
                @click="searchFromHistory(keyword)"
              >
                {{ keyword }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="banner-section">
      <div class="swiper-container">
        <div class="swiper-wrapper">
          <div 
            v-for="banner in banners" 
            :key="banner.id" 
            class="swiper-slide"
            @click="handleBannerClick(banner)"
          >
            <img :src="banner.image" alt="banner" class="banner-img" />
          </div>
        </div>
        <div class="swiper-pagination"></div>
      </div>
    </div>

    <div class="category-section px-4 py-4 bg-white mt-2">
      <div class="grid grid-cols-4 gap-4">
        <div 
          v-for="category in categories" 
          :key="category.id"
          class="category-item flex flex-col items-center"
          @click="goToCategory(category.id)"
        >
          <div class="category-icon w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center text-2xl mb-2">
            {{ category.icon }}
          </div>
          <span class="text-xs text-gray-700">{{ category.name }}</span>
        </div>
      </div>
    </div>

    <div class="hot-section px-4 py-4 mt-2 bg-white">
      <div class="section-title flex items-center justify-between mb-4">
        <h2 class="text-lg font-bold text-gray-800">热门推荐</h2>
        <span class="text-xs text-gray-500" @click="goToCategory(1)">查看更多 ></span>
      </div>
      <div class="hot-list flex overflow-x-auto gap-3 pb-2 -mx-4 px-4">
        <div 
          v-for="product in hotProducts" 
          :key="product.id"
          class="hot-product flex-shrink-0 w-28"
          @click="goToDetail(product.id)"
        >
          <img :src="product.cover" :alt="product.name" class="w-28 h-40 object-cover rounded-lg shadow-sm" />
          <p class="text-sm text-gray-800 mt-2 truncate">{{ product.name }}</p>
          <p class="text-sm text-primary font-bold mt-1">¥{{ product.price }}</p>
        </div>
      </div>
    </div>

    <div class="ranking-section px-4 py-4 mt-2 bg-white">
      <div class="section-title flex items-center justify-between mb-4">
        <h2 class="text-lg font-bold text-gray-800">热销榜单</h2>
      </div>
      <div class="ranking-list space-y-3">
        <div 
          v-for="(product, index) in rankingProducts" 
          :key="product.id"
          class="ranking-item flex items-center gap-3 p-2 rounded-lg hover:bg-gray-50"
          @click="goToDetail(product.id)"
        >
          <div 
            class="ranking-num w-6 h-6 rounded flex items-center justify-center text-sm font-bold"
            :class="index < 3 ? 'bg-primary text-white' : 'bg-gray-200 text-gray-600'"
          >
            {{ index + 1 }}
          </div>
          <img :src="product.cover" :alt="product.name" class="w-16 h-20 object-cover rounded" />
          <div class="flex-1">
            <p class="text-sm font-medium text-gray-800 truncate">{{ product.name }}</p>
            <p class="text-xs text-gray-500 mt-1">{{ product.author }}</p>
            <div class="flex items-center justify-between mt-1">
              <span class="text-sm text-primary font-bold">¥{{ product.price }}</span>
              <span class="text-xs text-gray-400">{{ product.rating }}分</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { categories, banners, getHotProducts, products, getProductsByKeyword } from '../data/books'

const router = useRouter()
const searchKeyword = ref('')
const showSearchHistory = ref(false)
const hotProducts = ref([])
const rankingProducts = ref([])
const searchHistory = ref(JSON.parse(localStorage.getItem('searchHistory') || '[]'))

const hotKeywords = ['T恤', '连衣裙', '运动鞋', '项链', '双肩包', '卫衣']

const searchSuggestions = computed(() => {
  if (!searchKeyword.value.trim()) return []
  return getProductsByKeyword(searchKeyword.value).slice(0, 5)
})

onMounted(() => {
  hotProducts.value = getHotProducts(10)
  rankingProducts.value = [...products].sort((a, b) => b.stock - a.stock).slice(0, 10)
  
  initSwiper()
  
  // 点击外部关闭搜索历史
  document.addEventListener('click', handleClickOutside)
})

const handleClickOutside = (e) => {
  const searchContainer = document.querySelector('.bg-primary')
  if (searchContainer && !searchContainer.contains(e.target)) {
    showSearchHistory.value = false
  }
}

const saveSearchHistory = (keyword) => {
  if (!keyword.trim()) return
  const history = searchHistory.value.filter(k => k !== keyword)
  history.unshift(keyword)
  searchHistory.value = history.slice(0, 10)
  localStorage.setItem('searchHistory', JSON.stringify(searchHistory.value))
}

const clearHistory = () => {
  searchHistory.value = []
  localStorage.removeItem('searchHistory')
}

const searchFromHistory = (keyword) => {
  searchKeyword.value = keyword
  handleSearch()
}

const handleInput = () => {
  // 实时搜索建议
}

const handleSearch = () => {
  if (searchKeyword.value.trim()) {
    saveSearchHistory(searchKeyword.value.trim())
    showSearchHistory.value = false
    router.push({ path: '/search', query: { keyword: searchKeyword.value } })
  }
}

const initSwiper = () => {
  let currentIndex = 0
  const wrapper = document.querySelector('.swiper-wrapper')
  const slides = document.querySelectorAll('.swiper-slide')
  const pagination = document.querySelector('.swiper-pagination')
  
  if (!wrapper || slides.length === 0) {
    setTimeout(initSwiper, 100)
    return
  }

  const slideCount = slides.length
  const interval = 3000

  const updatePagination = () => {
    pagination.innerHTML = ''
    for (let i = 0; i < slideCount; i++) {
      const dot = document.createElement('span')
      dot.className = `swiper-pagination-bullet ${i === currentIndex ? 'active' : ''}`
      dot.style.cssText = 'width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.5); margin: 0 3px; display: inline-block; cursor: pointer;'
      if (i === currentIndex) {
        dot.style.background = '#165DFF'
      }
      dot.addEventListener('click', () => {
        currentIndex = i
        updateSlide()
      })
      pagination.appendChild(dot)
    }
  }

  const updateSlide = () => {
    wrapper.style.transition = 'transform 0.5s ease'
    wrapper.style.transform = `translateX(-${currentIndex * 100}%)`
    updatePagination()
  }

  const autoPlay = () => {
    currentIndex = (currentIndex + 1) % slideCount
    updateSlide()
  }

  updatePagination()
  setInterval(autoPlay, interval)
}

const handleBannerClick = (banner) => {
  if (banner.link) {
    router.push(banner.link)
  }
}

const goToCategory = (categoryId) => {
  router.push({ path: '/category', query: { id: categoryId } })
}

const goToDetail = (bookId) => {
  router.push(`/book/${bookId}`)
}
</script>

<style scoped>
.banner-section {
  position: relative;
  overflow: hidden;
}

.swiper-container {
  position: relative;
  width: 100%;
  height: 150px;
}

.swiper-wrapper {
  display: flex;
  transition: transform 0.5s ease;
}

.swiper-slide {
  flex-shrink: 0;
  width: 100%;
  height: 100%;
}

.banner-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.swiper-pagination {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 6px;
}

:deep(.swiper-pagination-bullet) {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.5);
}

:deep(.swiper-pagination-bullet.active) {
  background: #165DFF;
}
</style>
