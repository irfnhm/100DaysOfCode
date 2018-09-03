#include <iostream>
#include <vector>

template <class _Type>
void rotateArrayOne(std::vector<_Type> vec, const _Type& _size){
    _Type temp{0};
    temp =  vec.at(_size - _size);
    for(_Type i = 0; i < _size - 1; ++i){
        vec.at(i) =  vec.at(i + 1);
        vec.at(_size - 1) =  temp;
    }
}

template <class T>
void rotateArray(std::vector<T> vec, const T& _size, const T& key){
    for (T i = 0; i < key; ++i){
        rotateArrayOne(vec, _size);
    }
    for(auto &i : vec){
        std::cout << i;
    }

}

int main(){
    std::vector<intmax_t> vec;
    intmax_t _size, key{2};
    std::cin >> _size;
    for(intmax_t i = 0; i < _size; ++i){
        intmax_t element;
        std::cin >> element;
        vec.push_back(element);
    }
    rotateArray(vec, _size, key);
    
}