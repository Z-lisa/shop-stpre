<template>
  <div class="min-h-screen bg-gray-50 pb-20">
    <div class="bg-primary px-4 py-3 flex items-center justify-between">
      <div class="flex items-center gap-3" @click="goBack">
        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        <span class="text-white text-lg">商品详情</span>
      </div>
      <div class="flex items-center gap-2">
        <div @click="handleShare" class="p-2">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
          </svg>
        </div>
        <div @click="toggleFavorite" class="p-2">
          <svg class="w-7 h-7" :class="isFavorite ? 'text-red-500' : 'text-white'" fill="currentColor" viewBox="0 0 24 24">
            <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" />
          </svg>
        </div>
      </div>
    </div>

    <div v-if="book" class="bg-white">
      <div class="relative">
        <div class="swiper-container overflow-hidden">
          <div class="flex transition-transform duration-300" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
            <div v-for="(img, index) in bookImages" :key="index" class="w-full flex-shrink-0">
              <img :src="img" :alt="book.name" class="w-full h-72 object-cover" />
            </div>
          </div>
        </div>
        <div class="absolute bottom-3 left-1/2 -translate-x-1/2 flex gap-2">
          <span 
            v-for="(_, index) in bookImages" 
            :key="index"
            class="w-2 h-2 rounded-full transition-colors"
            :class="currentSlide === index ? 'bg-primary' : 'bg-white/50'"
          ></span>
        </div>
      </div>

      <div class="p-4">
        <h1 class="text-lg font-bold text-gray-800">{{ book.name }}</h1>
        <div class="flex items-center gap-3 mt-2">
          <span class="text-2xl text-primary font-bold">¥{{ book.price }}</span>
          <span class="text-sm text-gray-400 line-through">¥{{ book.originalPrice }}</span>
        </div>
        <div class="flex items-center justify-between mt-3">
          <div class="flex items-center">
            <div class="flex items-center">
              <svg v-for="n in 5" :key="n" class="w-4 h-4" :class="n <= Math.floor(book.rating) ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8 2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292c.3.921-.755 1.688-1.54 1.118l1.07 3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
            </div>
            <span class="text-xs text-gray-400 ml-2">{{ book.rating }}分</span>
            <span class="text-xs text-gray-300 mx-2">|</span>
            <span v-if="book.sales" class="text-xs text-gray-400">已售 {{ book.sales }}本</span>
          </div>
        </div>
        <div v-if="book.tags && book.tags.length > 0" class="flex flex-wrap gap-2 mt-3">
          <span v-for="tag, index in book.tags" :key="index" class="px-2 py-1 bg-blue-50 text-primary text-xs rounded-full">
            {{ tag }}
          </span>
        </div>
      </div>

      <div class="px-4 py-3 border-t bg-orange-50 flex items-center gap-4">
        <div class="flex items-center gap-2">
          <span class="text-orange-500 text-lg">🎁</span>
          <span class="text-xs text-orange-600 font-medium">限时优惠</span>
        </div>
        <div class="flex-1 flex gap-2 overflow-x-auto">
          <span class="flex-shrink-0 px-2 py-0.5 bg-orange-500 text-white text-xs rounded">满59减10</span>
          <span class="flex-shrink-0 px-2 py-0.5 bg-orange-500 text-white text-xs rounded">满99减20</span>
          <span class="flex-shrink-0 px-2 py-0.5 bg-red-500 text-white text-xs rounded">赠书签</span>
        </div>
      </div>

      <div class="px-4 py-3 border-t flex items-center justify-between" @click="router.push('/coupons')">
        <div class="flex items-center gap-2">
          <span class="text-primary">🎫</span>
          <span class="text-sm text-gray-700">优惠券</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs text-primary">4张可用</span>
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </div>
      </div>

      <div class="px-4 py-3 border-t">
        <div class="flex items-center justify-between" @click="toggleDescription">
          <span class="text-sm font-medium text-gray-700">商品简介</span>
          <svg class="w-5 h-5 text-gray-400 transition-transform" :class="showDescription ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
        <transition name="slide">
          <div v-if="showDescription" class="mt-3 text-sm text-gray-600 leading-relaxed">
            {{ book.description }}
          </div>
        </transition>
      </div>

      <div class="px-4 py-3 border-t flex gap-6">
        <div class="flex-1 text-center" @click="showSize = true">
          <span class="text-sm text-primary">� 尺码</span>
        </div>
        <div class="w-px bg-gray-200"></div>
        <div class="flex-1 text-center" @click="showColor = true">
          <span class="text-sm text-gray-700">🎨 颜色</span>
        </div>
      </div>

      <div v-if="book.authorIntro" class="px-4 py-3 border-t">
        <div class="flex items-center justify-between" @click="toggleAuthorIntro">
          <span class="text-sm font-medium text-gray-700">品牌介绍</span>
          <svg class="w-5 h-5 text-gray-400 transition-transform" :class="showAuthorIntro ? 'rotate-180' : ''" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </div>
        <transition name="slide">
          <div v-if="showAuthorIntro" class="mt-3 text-sm text-gray-600 leading-relaxed">
            {{ book.authorIntro }}
          </div>
        </transition>
      </div>

      <div class="px-4 py-3 border-t">
        <span class="text-sm font-medium text-gray-700">商品规格</span>
        <div class="grid grid-cols-2 gap-4 text-sm mt-3">
          <div class="flex justify-between">
            <span class="text-gray-500">品牌</span>
            <span class="text-gray-800">{{ book.author }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">产地</span>
            <span class="text-gray-800">{{ book.publisher }}</span>
          </div>
          <div v-if="book.publishDate" class="flex justify-between">
            <span class="text-gray-500">生产日期</span>
            <span class="text-gray-800">{{ book.publishDate }}</span>
          </div>
          <div v-if="book.binding" class="flex justify-between">
            <span class="text-gray-500">材质</span>
            <span class="text-gray-800">{{ book.binding }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">库存</span>
            <span class="text-gray-800">{{ book.stock }}件</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500">评分</span>
            <span class="text-yellow-500">{{ book.rating }}分</span>
          </div>
        </div>
      </div>

      <div class="px-4 py-3 border-t">
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center gap-3">
            <span class="text-sm font-medium text-gray-700">用户评价</span>
            <div class="flex items-center gap-1">
              <svg v-for="n in 5" :key="n" class="w-4 h-4" :class="n <= Math.floor(averageRating) ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8 2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292c.3.921-.755 1.688-1.54 1.118l1.07 3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
              </svg>
              <span class="text-sm text-yellow-500">{{ averageRating.toFixed(1) }}</span>
            </div>
          </div>
          <span class="text-xs text-gray-400">{{ reviewsCount }}条评价</span>
        </div>
        
        <!-- 评价统计 -->
        <div class="flex items-center justify-between mb-4 text-xs text-gray-500">
          <span>好评率 {{ goodRatingRate }}%</span>
          <span @click="showAllReviews = true" class="text-primary cursor-pointer">查看全部评价</span>
        </div>
        
        <!-- 最新评价 -->
        <div class="space-y-4">
          <div v-for="(review, index) in displayedReviews" :key="index" class="pb-3 border-b last:border-0">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center text-sm text-white">{{ review.user.charAt(0) }}</div>
                <span class="text-sm text-gray-700">{{ review.user }}</span>
              </div>
              <div class="flex items-center gap-1">
                <svg v-for="n in 5" :key="n" class="w-3 h-3" :class="n <= review.rating ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8 2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292c.3.921-.755 1.688-1.54 1.118l1.07 3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
              </div>
            </div>
            <p class="text-sm text-gray-600 mt-2">{{ review.content }}</p>
            <div class="flex items-center justify-between mt-2">
              <p class="text-xs text-gray-400">{{ review.date }}</p>
              <div class="flex items-center gap-2">
                <button class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                  </svg>
                  {{ review.likes || 0 }}
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- 查看更多评价按钮 -->
        <button 
          v-if="allReviews.length > 5"
          class="w-full mt-4 px-4 py-2 border border-gray-200 text-gray-600 rounded-lg text-sm"
          @click="showAllReviews = true"
        >
          查看更多评价 ({{ allReviews.length }})
        </button>
        
        <!-- 添加评价按钮 -->
        <button 
          class="w-full mt-4 px-4 py-2 border border-primary text-primary rounded-lg text-sm font-medium"
          @click="showAddReview = true"
        >
          我要评价
        </button>
      </div>

      <div class="px-4 py-3 border-t">
        <span class="text-sm font-medium text-gray-700">物流/售后</span>
        <div class="mt-3 space-y-2 text-sm">
          <div class="flex items-center gap-2">
            <span class="text-green-500">🚚</span>
            <span class="text-gray-600">全国包邮，偏远地区除外</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-blue-500">📦</span>
            <span class="text-gray-600">48小时内发货</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-orange-500">🔄</span>
            <span class="text-gray-600">7天无理由退换</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="recommendBooks.length > 0" class="mt-2 bg-white px-4 py-3">
      <span class="text-sm font-medium text-gray-700">猜你喜欢</span>
      <div class="grid grid-cols-3 gap-3 mt-3">
        <div v-for="item in recommendBooks" :key="item.id" class="text-center" @click="router.push(`/book/${item.id}`)">
          <img :src="item.cover" :alt="item.name" class="w-full h-28 object-cover rounded" />
          <p class="text-xs text-gray-700 mt-2 line-clamp-2">{{ item.name }}</p>
          <p class="text-xs text-primary font-bold mt-1">¥{{ item.price }}</p>
        </div>
      </div>
    </div>

    <div v-else class="p-4 text-center text-gray-400">
      商品不存在
    </div>

    <div class="fixed bottom-14 left-0 right-0 bg-white border-t px-4 py-3 flex items-center gap-4" style="padding-bottom: calc(0.75rem + env(safe-area-inset-bottom));">
      <div class="flex items-center border rounded-lg flex-shrink-0">
        <button class="w-9 h-9 flex items-center justify-center text-gray-600" @click="decreaseQuantity">-</button>
        <span class="w-10 text-center text-gray-800">{{ quantity }}</span>
        <button class="w-9 h-9 flex items-center justify-center text-gray-600" @click="increaseQuantity">+</button>
      </div>
      <button class="flex-1 h-11 rounded-lg border border-primary text-primary font-medium" @click="handleAddToCart">
        加入购物车
      </button>
      <button class="flex-1 h-11 rounded-lg bg-primary text-white font-medium" @click="handleBuyNow">
        立即购买
      </button>
    </div>

    <div v-if="showSize" class="fixed inset-0 bg-black/50 z-100 flex items-end" @click.self="showSize = false">
      <div class="bg-white w-full rounded-t-2xl max-h-[70vh] overflow-hidden">
        <div class="flex items-center justify-between px-4 py-3 border-b">
          <span class="text-lg font-bold">尺码选择</span>
          <button @click="showSize = false">
            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="p-4 overflow-y-auto max-h-[60vh]">
          <div class="text-sm text-gray-600 mb-4">请选择合适的尺码，测量数据仅供参考</div>
          <div class="grid grid-cols-4 gap-3">
            <button 
              v-for="size in ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL']" 
              :key="size"
              class="py-3 border rounded-lg text-sm transition-all"
              :class="selectedSize === size ? 'border-primary bg-primary/10 text-primary' : 'border-gray-200 text-gray-700 hover:border-gray-300'"
              @click="selectedSize = size"
            >
              {{ size }}
            </button>
          </div>
          <div class="mt-6">
            <div class="text-sm font-medium text-gray-700 mb-3">尺码参考表</div>
            <table class="w-full text-sm border">
              <thead class="bg-gray-50">
                <tr>
                  <th class="py-2 px-3 text-left text-gray-600">尺码</th>
                  <th class="py-2 px-3 text-left text-gray-600">胸围</th>
                  <th class="py-2 px-3 text-left text-gray-600">衣长</th>
                  <th class="py-2 px-3 text-left text-gray-600">袖长</th>
                </tr>
              </thead>
              <tbody>
                <tr class="border-t">
                  <td class="py-2 px-3">S</td>
                  <td class="py-2 px-3">90cm</td>
                  <td class="py-2 px-3">65cm</td>
                  <td class="py-2 px-3">57cm</td>
                </tr>
                <tr class="border-t">
                  <td class="py-2 px-3">M</td>
                  <td class="py-2 px-3">95cm</td>
                  <td class="py-2 px-3">67cm</td>
                  <td class="py-2 px-3">58cm</td>
                </tr>
                <tr class="border-t">
                  <td class="py-2 px-3">L</td>
                  <td class="py-2 px-3">100cm</td>
                  <td class="py-2 px-3">69cm</td>
                  <td class="py-2 px-3">59cm</td>
                </tr>
                <tr class="border-t">
                  <td class="py-2 px-3">XL</td>
                  <td class="py-2 px-3">105cm</td>
                  <td class="py-2 px-3">71cm</td>
                  <td class="py-2 px-3">60cm</td>
                </tr>
              </tbody>
            </table>
          </div>
          <button class="w-full mt-6 py-3 bg-primary text-white rounded-lg" @click="showSize = false">
            确定
          </button>
        </div>
      </div>
    </div>

    <div v-if="showColor" class="fixed inset-0 bg-black/50 z-100 flex items-end" @click.self="showColor = false">
      <div class="bg-white w-full rounded-t-2xl max-h-[70vh] overflow-hidden">
        <div class="flex items-center justify-between px-4 py-3 border-b">
          <span class="text-lg font-bold">颜色选择</span>
          <button @click="showColor = false">
            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="p-4 overflow-y-auto max-h-[60vh]">
          <div class="grid grid-cols-3 gap-4">
            <button 
              v-for="color in colorOptions" 
              :key="color.name"
              class="flex flex-col items-center p-3 border rounded-lg transition-all"
              :class="selectedColor === color.name ? 'border-primary bg-primary/10' : 'border-gray-200 hover:border-gray-300'"
              @click="selectedColor = color.name"
            >
              <div class="w-12 h-12 rounded-full border mb-2" :style="{ backgroundColor: color.hex }"></div>
              <span class="text-sm text-gray-700">{{ color.name }}</span>
            </button>
          </div>
          <button class="w-full mt-6 py-3 bg-primary text-white rounded-lg" @click="showColor = false">
            确定
          </button>
        </div>
      </div>
    </div>

    <!-- 全部评价弹窗 -->
    <div v-if="showAllReviews" class="fixed inset-0 bg-black/50 z-100" @click.self="showAllReviews = false">
      <div class="fixed bottom-0 left-0 right-0 bg-white rounded-t-2xl max-h-[80vh] overflow-y-auto z-100">
        <div class="sticky top-0 bg-white px-4 py-3 border-b flex items-center justify-between">
          <span class="text-lg font-bold">全部评价</span>
          <button @click="showAllReviews = false">
            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="p-4 space-y-4">
          <div v-for="(review, index) in allReviews" :key="index" class="pb-3 border-b last:border-0">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center text-sm text-white">{{ review.user.charAt(0) }}</div>
                <span class="text-sm text-gray-700">{{ review.user }}</span>
              </div>
              <div class="flex items-center gap-1">
                <svg v-for="n in 5" :key="n" class="w-3 h-3" :class="n <= review.rating ? 'text-yellow-400' : 'text-gray-300'" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8 2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292c.3.921-.755 1.688-1.54 1.118l1.07 3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                </svg>
              </div>
            </div>
            <p class="text-sm text-gray-600 mt-2">{{ review.content }}</p>
            <div class="flex items-center justify-between mt-2">
              <p class="text-xs text-gray-400">{{ review.date }}</p>
              <div class="flex items-center gap-2">
                <button class="text-xs text-gray-400 flex items-center gap-1">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
                  </svg>
                  {{ review.likes || 0 }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 添加评价弹窗 -->
    <div v-if="showAddReview" class="fixed inset-0 bg-black/50 z-100" @click.self="showAddReview = false">
      <div class="fixed bottom-0 left-0 right-0 bg-white rounded-t-2xl max-h-[80vh] overflow-y-auto z-100">
        <div class="sticky top-0 bg-white px-4 py-3 border-b flex items-center justify-between">
          <span class="text-lg font-bold">添加评价</span>
          <button @click="showAddReview = false">
            <svg class="w-6 h-6 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="p-4 space-y-4">
          <div>
            <label class="block text-sm text-gray-600 mb-3">评分</label>
            <div class="flex gap-2">
              <button 
                v-for="n in 5" 
                :key="n"
                class="w-10 h-10 rounded-full flex items-center justify-center text-2xl transition-colors"
                :class="n <= newReview.rating ? 'text-yellow-400' : 'text-gray-300'"
                @click="newReview.rating = n"
              >
                ⭐
              </button>
            </div>
          </div>
          
          <div>
            <label class="block text-sm text-gray-600 mb-2">评价内容</label>
            <textarea 
              v-model="newReview.content"
              placeholder="请输入您的评价..."
              rows="4"
              class="w-full px-4 py-3 border border-gray-200 rounded-lg text-sm resize-none"
            ></textarea>
          </div>
          
          <button 
            class="w-full h-12 rounded-lg bg-primary text-white font-medium"
            :disabled="!newReview.content"
            :class="!newReview.content ? 'opacity-50' : ''"
            @click="submitReview"
          >
            提交评价
          </button>
        </div>
      </div>
    </div>

    <transition name="fade">
      <div v-if="showToast" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-gray-800 text-white px-6 py-3 rounded-lg text-sm z-100">
        {{ toastMessage }}
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getProductById, categories, getRecommendProducts } from '../data/books'
import { useCartStore } from '../stores/cart'
import { useFavoritesStore } from '../stores/favorites'
import { useReviewsStore } from '../stores/reviews'
import { useUserStore } from '../stores/user'

const route = useRoute()
const router = useRouter()
const cartStore = useCartStore()
const favoritesStore = useFavoritesStore()
const reviewsStore = useReviewsStore()
const userStore = useUserStore()

const book = ref(null)
const showDescription = ref(true)
const showAuthorIntro = ref(false)
const showSize = ref(false)
const showColor = ref(false)
const showAllReviews = ref(false)
const showAddReview = ref(false)
const quantity = ref(1)
const showToast = ref(false)
const toastMessage = ref('')
const currentSlide = ref(0)
const selectedSize = ref('')
const selectedColor = ref('')
const colorOptions = ref([
  { name: '白色', hex: '#FFFFFF' },
  { name: '黑色', hex: '#1A1A1A' },
  { name: '灰色', hex: '#9CA3AF' },
  { name: '藏青色', hex: '#1E3A5F' },
  { name: '红色', hex: '#DC2626' },
  { name: '蓝色', hex: '#3B82F6' },
  { name: '绿色', hex: '#22C55E' },
  { name: '粉色', hex: '#EC4899' },
  { name: '米色', hex: '#D4C4A8' }
])
const newReview = ref({
  rating: 5,
  content: ''
})
let slideTimer = null

const bookImages = computed(() => {
  if (!book.value) return []
  return [
    book.value.cover,
    book.value.cover,
    book.value.cover
  ]
})

// 合并原始评价和新增评价
const allReviews = computed(() => {
  if (!book.value) return []
  const originalReviews = book.value.reviews || []
  const newReviews = reviewsStore.getBookReviews(book.value.id)
  return [...newReviews, ...originalReviews]
})

const reviewsCount = computed(() => allReviews.value.length)

const averageRating = computed(() => {
  if (allReviews.value.length === 0) return 0
  const total = allReviews.value.reduce((sum, review) => sum + review.rating, 0)
  return total / allReviews.value.length
})

const goodRatingRate = computed(() => {
  if (allReviews.value.length === 0) return 0
  const goodCount = allReviews.value.filter(review => review.rating >= 4).length
  return Math.round((goodCount / allReviews.value.length) * 100)
})

const displayedReviews = computed(() => {
  return allReviews.value.slice(0, 5)
})

const recommendBooks = computed(() => {
  if (!book.value) return []
  return getRecommendProducts(book.value.id, 6)
})

const isFavorite = computed(() => {
  return book.value ? favoritesStore.isFavorite(book.value.id) : false
})

const goBack = () => {
  router.back()
}

const toggleDescription = () => {
  showDescription.value = !showDescription.value
}

const toggleAuthorIntro = () => {
  showAuthorIntro.value = !showAuthorIntro.value
}

const decreaseQuantity = () => {
  if (quantity.value > 1) {
    quantity.value--
  }
}

const increaseQuantity = () => {
  if (quantity.value < 99) {
    quantity.value++
  }
}

const toggleFavorite = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再收藏')
    return
  }
  if (book.value) {
    const wasFavorite = favoritesStore.isFavorite(book.value.id)
    favoritesStore.toggleFavorite(book.value)
    showToastMessage(wasFavorite ? '已取消收藏' : '收藏成功')
  }
}

const handleShare = () => {
  showToastMessage('分享功能开发中')
}

const showToastMessage = (message) => {
  toastMessage.value = message
  showToast.value = true
  setTimeout(() => {
    showToast.value = false
  }, 1500)
}

const handleAddToCart = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再加入购物车')
    return
  }
  if (book.value) {
    cartStore.addToCart(book.value, quantity.value)
    showToastMessage('已加入购物车')
  }
}

const handleBuyNow = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再下单')
    return
  }
  if (book.value) {
    cartStore.addToCart(book.value, quantity.value)
    router.push('/checkout')
  }
}

const submitReview = () => {
  if (!userStore.isLoggedIn) {
    showToastMessage('请先登录后再评价')
    return
  }
  if (!book.value || !newReview.value.content.trim()) {
    showToastMessage('请输入评价内容')
    return
  }
  
  const review = {
    rating: newReview.value.rating,
    content: newReview.value.content.trim()
  }
  
  reviewsStore.addReview(book.value.id, review)
  
  // 重置表单
  newReview.value.rating = 5
  newReview.value.content = ''
  
  // 关闭弹窗
  showAddReview.value = false
  
  showToastMessage('评价提交成功')
}

const startSlideTimer = () => {
  slideTimer = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % bookImages.value.length
  }, 3000)
}

const stopSlideTimer = () => {
  if (slideTimer) {
    clearInterval(slideTimer)
    slideTimer = null
  }
}

onMounted(() => {
  const bookId = route.params.id
  if (bookId) {
    book.value = getProductById(Number(bookId))
  }
  startSlideTimer()
})

onUnmounted(() => {
  stopSlideTimer()
})
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
  max-height: 500px;
  overflow: hidden;
}
.slide-enter-from,
.slide-leave-to {
  max-height: 0;
  opacity: 0;
}
</style>
