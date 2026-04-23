import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const cartItems = ref(JSON.parse(localStorage.getItem('cart') || '[]'))
  const selectedItems = ref(JSON.parse(localStorage.getItem('selectedItems') || '[]'))

  const saveToLocalStorage = () => {
    localStorage.setItem('cart', JSON.stringify(cartItems.value))
    localStorage.setItem('selectedItems', JSON.stringify(selectedItems.value))
  }

  const totalItems = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + item.quantity, 0)
  })

  const totalPrice = computed(() => {
    return cartItems.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  })

  const selectedTotal = computed(() => {
    return cartItems.value
      .filter(item => selectedItems.value.includes(item.id))
      .reduce((sum, item) => sum + item.price * item.quantity, 0)
  })

  const selectedCount = computed(() => {
    return cartItems.value
      .filter(item => selectedItems.value.includes(item.id))
      .reduce((sum, item) => sum + item.quantity, 0)
  })

  const isAllSelected = computed(() => {
    return cartItems.value.length > 0 && 
           cartItems.value.every(item => selectedItems.value.includes(item.id))
  })

  const addToCart = (book, quantity = 1) => {
    const existingItem = cartItems.value.find(item => item.id === book.id)
    if (existingItem) {
      existingItem.quantity += quantity
    } else {
      cartItems.value.push({
        id: book.id,
        name: book.name,
        author: book.author,
        price: book.price,
        cover: book.cover,
        quantity: quantity,
        stock: book.stock
      })
      selectedItems.value.push(book.id)
    }
    saveToLocalStorage()
  }

  const removeFromCart = (bookId) => {
    const index = cartItems.value.findIndex(item => item.id === bookId)
    if (index > -1) {
      cartItems.value.splice(index, 1)
      selectedItems.value = selectedItems.value.filter(id => id !== bookId)
      saveToLocalStorage()
    }
  }

  const updateQuantity = (bookId, quantity) => {
    const item = cartItems.value.find(item => item.id === bookId)
    if (item) {
      item.quantity = Math.max(1, Math.min(99, quantity))
      saveToLocalStorage()
    }
  }

  const toggleSelect = (bookId) => {
    const index = selectedItems.value.indexOf(bookId)
    if (index > -1) {
      selectedItems.value.splice(index, 1)
    } else {
      selectedItems.value.push(bookId)
    }
    saveToLocalStorage()
  }

  const selectAll = () => {
    if (isAllSelected.value) {
      selectedItems.value = []
    } else {
      selectedItems.value = cartItems.value.map(item => item.id)
    }
    saveToLocalStorage()
  }

  const clearCart = () => {
    cartItems.value = []
    selectedItems.value = []
    saveToLocalStorage()
  }

  const getSelectedItems = () => {
    return cartItems.value.filter(item => selectedItems.value.includes(item.id))
  }

  return {
    cartItems,
    selectedItems,
    totalItems,
    totalPrice,
    selectedTotal,
    selectedCount,
    isAllSelected,
    addToCart,
    removeFromCart,
    updateQuantity,
    toggleSelect,
    selectAll,
    clearCart,
    getSelectedItems
  }
})
