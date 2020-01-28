[![CircleCI](https://circleci.com/gh/proteneer/timemachine.svg?style=svg&circle-token=d4635916d6394573ebda0aa17a63540bc8b449fc)](https://circleci.com/gh/proteneer/timemachine)

# Time Machine

The TimeMachine is a simplified and differentiable MD engine with the following features:

1. Optimized for performance on modern NVIDIA GPUs.
2. Analytical first order derivatives of the potential with respect to the coordinates and the forcefield parameters.
3. Analytical second order hessian vector products of the above at a 2.5x cost.
4. Implements adjoint equations of motion via rematerialization, enabling one to differentiate objective functions with respect to an arbitrary number of forcefield parameters in a *single* backwards pass.

The code is implemented against OpenMM and is still under very heavy development.

# License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
