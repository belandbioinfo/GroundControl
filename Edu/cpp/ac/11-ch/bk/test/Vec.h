#ifndef GUARD_VEC_H
#define GUARD_VEC_H

// Vec is a vector -alike class
//

#include <memory>

template <class T> class Vec{
public:
    typedef T* iterator;
    typedef const T* const_iterator;
    typedef std::size_t size_type;
    typedef T value_type;
    typedef T& reference;
    typedef const T& const_reference;

    // default constructor
    Vec() { create(); }

    // constructor with parameters
    explicit Vec(size_type n, const T& t = T()) { create(n, t); }

    // copy constructor
    Vec(const Vec& v) { create(v.begin(), v.end()); }

    // assignment operator
    Vec& operator=(const Vec&);

    // destructor
    ~Vec() { uncreate(); }

    // index operator
    T& operator[](size_type i) const { return data[i]; }

    // push back member function
    void push_back(const T& t) {
        if (avail == limit)
            grow();
        unchecked_append(t);
    }

    // size accessor member function
    size_type size() const { return avail - data; }

    // iterator accessor member functions
    iterator begin() { return data; }
    const_iterator begin() const { return data; }

    iterator end() { return avail; }
    const_iterator end() const { return avail; }

    iterator erase(iterator pos) { 
        iterator ret;
        for (iterator b = pos; b+1 != avail; b++) {
            *b = *(b+1);
        }
        alloc.destroy(avail--);
        return pos+1;
    }

    void clear() {
        if (data) {
            // destroy (in reverse order) the elements that were constructed
            iterator it = avail;
            while (it != data) 
                alloc.destroy(--it);
        }
        // reset pointers to indicate that the Vec is empty again
        data = avail = 0;
    }

private:
    iterator data;    // first element in the Vec
    iterator avail;   // one past the last element in the Vec
    iterator limit;   // one past the allocated memory

    // facilities for memory allocation
    std::allocator<T> alloc;

    void create() {
        data = avail = limit = 0;
    }
    
    void create(size_type n, const T& val) {
        data = alloc.allocate(n);
        limit = avail = data + n;
        std::uninitialized_fill(data, limit, val);
    }
    
    void create(const_iterator i, const_iterator j) {
        data = alloc.allocate(j-i);
        limit = avail = std::uninitialized_copy(i, j, data);
    }
    
    void uncreate() {
        if (data) {
            // destroy (in reverse order) the elements that were constructed
            iterator it = avail;
            while (it != data) 
                alloc.destroy(--it);
    
            // return all the space that was allocated
            alloc.deallocate(data, limit - data);
        }
        // reset pointers to indicate that the Vec is empty again
        data = limit = avail = 0;
    
    }
    
    void grow() {
        // when growing, allocate twice as much space as currently in use
        size_type new_size = std::max(2 * (limit - data), std::ptrdiff_t(1));
    
        // allocate new space and copy existing elements to the new space
        iterator new_data = alloc.allocate(new_size);
        iterator new_avail = std::uninitialized_copy(data, avail, new_data);
    
        // return the old space
        uncreate();
    
        // reset pointers to point to the newly allocated space
        data = new_data;
        avail = new_avail;
        limit = data + new_size;
    }
    
    // assumes avail points at allocated, but uninitialized space
    void unchecked_append(const T& val) {
        alloc.construct(avail++, val);
    }
    
};

#endif
