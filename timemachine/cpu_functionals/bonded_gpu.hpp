#pragma once

#include "energy.hpp"
#include <vector>

namespace timemachine {


template <typename NumericType>
class HarmonicBondGPU: public EnergyGPU<NumericType> {

private:

    NumericType* d_params_;
    int* d_global_param_idxs_;
    int* d_param_idxs_;
    int* d_bond_idxs_;
    int n_bonds_;
    int P_;

public:

    HarmonicBondGPU(
        std::vector<NumericType> params,
        std::vector<size_t> global_param_idxs,
        std::vector<size_t> param_idxs,
        std::vector<size_t> bond_idxs
    );

    ~HarmonicBondGPU();

    void set_params(const std::vector<NumericType> &new_params);

    std::vector<NumericType> get_params() const;

    void total_derivative(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

    void total_derivative_cpu(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

};


template <typename NumericType>
class HarmonicAngleGPU: public EnergyGPU<NumericType> {

private:

    NumericType* d_params_;
    int* d_global_param_idxs_;
    int* d_param_idxs_;
    int* d_angle_idxs_;
    int n_angles_;
    int P_;

public:

    HarmonicAngleGPU(
        std::vector<NumericType> params,
        std::vector<size_t> global_param_idxs,
        std::vector<size_t> param_idxs,
        std::vector<size_t> angle_idxs
    );

    ~HarmonicAngleGPU();

    void set_params(const std::vector<NumericType> &new_params);

    std::vector<NumericType> get_params() const;

    void total_derivative(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

    void total_derivative_cpu(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

};


template <typename NumericType>
class PeriodicTorsionGPU: public EnergyGPU<NumericType> {

private:

    NumericType* d_params_;
    int* d_global_param_idxs_;
    int* d_param_idxs_;
    int* d_torsion_idxs_;
    int n_torsions_;
    int P_;

public:

    PeriodicTorsionGPU(
        std::vector<NumericType> params,
        std::vector<size_t> global_param_idxs,
        std::vector<size_t> param_idxs,
        std::vector<size_t> torsion_idxs
    );

    ~PeriodicTorsionGPU();

    void set_params(const std::vector<NumericType> &new_params);

    std::vector<NumericType> get_params() const;

    void total_derivative(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

    void total_derivative_cpu(
        const size_t n_atoms,
        const size_t n_params,
        const NumericType* d_coords, // [N, 3]
        NumericType* d_energy_out, // []
        NumericType* d_grad_out, // [N,3]
        NumericType* d_hessian_out, // [N, 3, N, 3]
        NumericType* d_mp_out // [P, N, 3]
    );

};


}
