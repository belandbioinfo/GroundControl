// Handle Class

template <class T>
Handle<T>& Handle<T>::operator=(const Handle& rhs)
{
    if (&rhs != this){
        delete p;
        p = rhs.p ? rhs.p->clone() : 0;
    }
    return *this;
}
