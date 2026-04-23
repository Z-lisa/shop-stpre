import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useFavoritesStore = defineStore('favorites', () => {
  const favorites = ref(JSON.parse(localStorage.getItem('favorites') || '[]'))

  const saveToLocalStorage = () => {
    localStorage.setItem('favorites', JSON.stringify(favorites.value))
  }

  const isFavorite = (bookId) => {
    return favorites.value.some(item => item.id === bookId)
  }

  const addFavorite = (book) => {
    if (!isFavorite(book.id)) {
      favorites.value.push({
        id: book.id,
        name: book.name,
        author: book.author,
        price: book.price,
        cover: book.cover,
        rating: book.rating
      })
      saveToLocalStorage()
    }
  }

  const removeFavorite = (bookId) => {
    const index = favorites.value.findIndex(item => item.id === bookId)
    if (index > -1) {
      favorites.value.splice(index, 1)
      saveToLocalStorage()
    }
  }

  const toggleFavorite = (book) => {
    if (isFavorite(book.id)) {
      removeFavorite(book.id)
    } else {
      addFavorite(book)
    }
  }

  const favoritesCount = computed(() => favorites.value.length)

  return {
    favorites,
    isFavorite,
    addFavorite,
    removeFavorite,
    toggleFavorite,
    favoritesCount
  }
})
